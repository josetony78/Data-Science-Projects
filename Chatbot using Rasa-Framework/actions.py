from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted
from collections import OrderedDict
import zomatopy
import json
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

class ActionValidateLocation(Action):
    def name(self):
        return 'action_validate_location'

    def run(self, dispatcher, tracker, domain):
        list_loc = ["ahmedabad","bangalore","chennai","delhi","hyderabad","kolkata","mumbai","pune","agra","ajmer","aligarh","allahabad","amravati","amritsar",
"asansol","aurangabad","bareilly","belgaum","bhavnagar","bhiwandi","bhopal","bhubaneswar","bikaner","bokaro steel city","chandigarh","coimbatore","cuttack","dehradun","dhanbad","durg-bhilai nagar","durgapur","erode","faridabad","firozabad","ghaziabad","gorakhpur","gulbarga","guntur","gurgaon","guwahati","hubli-dharwad","indore","jabalpur","jaipur","jalandhar","jammu","jamnagar","jamshedpur","jhansi","jodhpur","kannur","kanpur","kakinada",
"kochi","kottayam","kolhapur","kollam","kota","kozhikode","kurnool","lucknow","ludhiana","madurai","malappuram","mathura","goa","mangalore","meerut","moradabad","mysore","nagpur","nanded","nashik","nellore","noida","palakkad","patna","pondicherry","raipur","rajkot","rajahmundry","ranchi","rourkela","salem","sangli","siliguri","solapur","srinagar","sultanpur","surat","thiruvananthapuram","thrissur","tiruchirappalli","tirunelveli","tiruppur","ujjain","vijayapura","vadodara","varanasi","vasai-virar city","vijayawada","visakhapatnam","warangal","gwalior"]
        loc = tracker.get_slot('location')
        if loc is not None:
            if loc.lower() in list_loc:
                return[SlotSet('location',loc)]
            else:
                dispatcher.utter_message("Sorry we do not operate in this area yet. try some other location")
                return[SlotSet('location',None)]
        else:
            dispatcher.utter_message("Sorry I could not understand the location you provided. try some other location")
            return[SlotSet('location', None)]

class ActionValidateCuisine(Action):
    def name(self):
        return 'action_validate_cuisine'
    
    def run(self, dispatcher, tracker, domain):
        list_cuisine = ["chinese","mexican","american","italian","south indian","north indian"]
        cuisine = tracker.get_slot('cuisine')
        if cuisine is not None:
            if cuisine.lower() in list_cuisine:
                return[SlotSet('cuisine',cuisine)]
            #elif cuisine == 0 or :
            else:
                dispatcher.utter_message("Sorry this is not a valid cuisine. please check for typing errors")
                return[SlotSet('cuisine',None)]
        else:
            dispatcher.utter_message("Sorry I could not understand the cuisine name you provided")
            return[SlotSet('cuisine', None)]

class ActionValidateBudget(Action):
    def name(self):
        return 'action_validate_budget'

    def run(self, dispatcher, tracker, domain):
        cost_queried = tracker.get_slot('budget')
        if cost_queried == 'less than 300' or cost_queried == 'lesser than 300' or cost_queried == '< 300' or ("cheap" in cost_queried) or ("cheaper" in cost_queried) or ("cheapest" in cost_queried) or cost_queried == 'Less than Rs. 300':
            return[SlotSet('budget', 'low')]
        elif cost_queried == 'more than 700' or cost_queried == 'greater than 700' or cost_queried == '> 700' or ("costly" in cost_queried) or ("expensive" in cost_queried) or cost_queried == 'More than 700':
            return[SlotSet('budget', 'high')]
        else:
            return[SlotSet('budget', 'mid')] #always return mid budget by default
        
#         elif cost_queried == 'between 300 and 700' or cost_queried == '300-700' or cost_queried == '< 700' or ("moderate" in cost_queried) or ("medium" in cost_queried) or ("moderately" in cost_queried) or ("Average" in cost_queried) or ("in between 300 & 700" in cost_queried) or cost_queried == 'Rs. 300-700':
#             return[SlotSet('budget', 'mid')]
#         else:
#             return[SlotSet('budget',None)]
#         else:
#             return[SlotSet('budget', 'mid')] #always return mid budget by default

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"ae9a5f3d4c6e92c68d90870962cb3562"}#type your zomato API key here
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        cuisine = cuisine.lower()
        #budget1 = tracker.get_slot('budget')
        #budget = 'average cost for two ' + str(budget1)
        budget = tracker.get_slot('budget')
        if budget == 'low':
            cost_to_filer_min = 0
            cost_to_filer_max = 300
        elif budget == 'mid':
            cost_to_filer_min = 301
            cost_to_filer_max = 700
        elif budget == 'high':
            cost_to_filer_min = 701
            cost_to_filer_max = 9999
        cols = ['restaurant name', 'restaurant address', 'avg. budget for two', 'zomato rating']
        resrnt_df = pd.DataFrame(columns = cols)
        location_detail=zomato.get_location(loc, 1)
        #print(location_detail)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north indian':50,'south indian':85}
        #results=zomato.restaurant_search(str(budget), lat, lon, str(cuisines_dict.get(cuisine)),"rating","desc", 20)
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),"rating","desc", 20)#get first 20 and filter budget later
        response=""
        for i in range(0,5, 1):
            d = json.loads(results[i])
            if d['results_found'] != 0:
                #print(json.dumps(d, indent=2))
                for restaurant in d['restaurants']:
                    curr_res = {'zomato rating':restaurant['restaurant']["user_rating"]["aggregate_rating"],'restaurant name':restaurant['restaurant']['name'],'restaurant address': restaurant['restaurant']['location']['address'], 'avg. budget for two': restaurant['restaurant']['average_cost_for_two']}		
                    if (curr_res['avg. budget for two'] >= cost_to_filer_min) and (curr_res['avg. budget for two'] <= cost_to_filer_max):
                        resrnt_df.loc[len(resrnt_df)] = curr_res
            #print(len(resrnt_df))
        # sort restarants on aggregate rating  
        resrnt_df = resrnt_df.sort_values(['zomato rating','avg. budget for two'], ascending=[False,True])
        resrnt_df10 = resrnt_df.head(10)
        resrnt_df = resrnt_df.head(5)
        resrnt_df = resrnt_df.reset_index(drop=True)
        resrnt_df.index = resrnt_df.index.map(str)
        # print to console in format
        if len(resrnt_df) != 0:
            for index, row in resrnt_df.iterrows():
                response = response+ index + ". Found \""+ row['restaurant name']+ "\" in "+ row['restaurant address']+" has been rated "+ row['zomato rating']+"\n"
        else:
            response = 'Found 0 restaurants in given price range'
        #print(response)
        dispatcher.utter_message(response)
        return [SlotSet('budget',budget)]

class ActionValidateEmail(Action):
    def name(self):
        return 'action_validate_email'
        
    def run(self, dispatcher, tracker, domain):
        pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        email_check = tracker.get_slot('email')
        if email_check is not None:
            if re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email_check):
                return[SlotSet('email',email_check)]
            else:
                dispatcher.utter_message("Sorry this is not a valid email. please check for typing errors")
                return[SlotSet('email',None)]
        else:
            dispatcher.utter_message("Sorry I could not understand the email address which you provided? Please provide again")
            return[SlotSet('email', None)]

class ActionSendEmail(Action):
    def name(self):
        return 'action_email'
    
    def run(self, dispatcher, tracker, domain):
        config={"user_key":"ae9a5f3d4c6e92c68d90870962cb3562"}#type your zomato API key here
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        cuisine = cuisine.lower()
        budget = tracker.get_slot('budget')
        # budget = 'average cost for two ' + str(budget)
        if budget == 'low':
            cost_to_filer_min = 0
            cost_to_filer_max = 300
        elif budget == 'mid':
            cost_to_filer_min = 301
            cost_to_filer_max = 700
        elif budget == 'high':
            cost_to_filer_min = 701
            cost_to_filer_max = 9999
        cols = ['restaurant name', 'restaurant address', 'avg. budget for two', 'zomato rating']
        resrnt_df = pd.DataFrame(columns = cols)	
        location_detail=zomato.get_location(loc, 1)
        #print(location_detail)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north indian':50,'south indian':85}
        #results=zomato.restaurant_search(str(budget), lat, lon, str(cuisines_dict.get(cuisine)),"rating","desc", 20)
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),"rating","desc", 20)
        response=""
        for i in range(0,5, 1):
            d = json.loads(results[i])
            if d['results_found'] != 0:
                #print(json.dumps(d, indent=2))
                for restaurant in d['restaurants']:
                    curr_res = {'zomato rating':restaurant['restaurant']["user_rating"]["aggregate_rating"], 'restaurant name':restaurant['restaurant']['name'], 'restaurant address': restaurant['restaurant']['location']['address'], 'avg. budget for two': restaurant['restaurant']['average_cost_for_two']}
                    if (curr_res['avg. budget for two'] >= cost_to_filer_min) and (curr_res['avg. budget for two'] <= cost_to_filer_max):
                        resrnt_df.loc[len(resrnt_df)] = curr_res
            #print(len(resrnt_df))
        # sort restarants on aggregate rating  
        resrnt_df = resrnt_df.sort_values(['zomato rating','avg. budget for two'], ascending=[False,True])
        email = tracker.get_slot('email')
        gmail_user = 'josetony78dsgcp@gmail.com'  #typr your email id here
        gmail_password = 'Pranab1!' #typr your password here
        sent_from = gmail_user  
        to = str(email)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Restaurant Details"
        msg['From'] = gmail_user
        msg['To'] = to
        if len(resrnt_df) == 0:
            html = """
            <html>
            <head>
            <style>
            table {
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }

            td, th {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }
            tr:nth-child(even) {
                background-color: #dddddd;
            }
            </style>
            </head>
            <body>
            <p>Hi!</p>
            <p>Thanks for using Foodie, the restaurant chatbot.</p>
            <p>Sorry, we could not find restaurant that meet your criteria.</p>
            """
        else:
            resrnt_df10 = resrnt_df.head(10)
            resrnt_df10 = resrnt_df10.reset_index(drop=True)
            resrnt_df10.index = resrnt_df10.index.map(str)
            html = """
            <html>
            <head>
            <style>
            table {
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }
            td, th {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }
            tr:nth-child(even) {
                background-color: #dddddd;
            }
            </style>
            </head>
            <body>
            <p>Hi!</p>
            <p>Thanks for using Foodie, the restaurant chatbot. Please find the requested list of restaurants below.</p>
            <p>Enjoy the food!</p>
            """	
            html = html+resrnt_df10.to_html()
        html = html+"<p> based on your query...</p>"+cuisine+" restaurants "+budget+" budget at "+loc+"</body></html>"
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, msg.as_string())
        server.close()
        dispatcher.utter_message("Email Sent")
        return [SlotSet('email',email)]

class ActionRestarted(Action):
    def name(self):
        return 'action_restarted'
    def run(self, dispatcher, tracker, domain): 
        return[Restarted()]