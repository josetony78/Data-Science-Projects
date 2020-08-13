## UserGaveLocationCuisineBudgetAndDeniedEmailing
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - utter_ask_budget
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - action_validate_budget
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_ask_about_emailing
* deny
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
* goodbye
    - action_restarted
    
## UserGaveLocationCuisineBudgetAndAffirmedEmailing
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese", "location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Mumbai"}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"budget": "mid"}
    - utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "josetony78@gmail.com"}
    - slot{"email": "josetony78@gmail.com"}
    - action_email
    - slot{"email": "josetony78@gmail.com"}
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
* goodbye
    - action_restarted

## UserGreetedAndThenDenying
* greet
    - utter_greet
* deny
    - utter_default
* deny
    - utter_default
* deny
    - utter_goodbye
    - action_restarted

## Provided location first time is not tier-1 and tier-2 city
* greet
    - utter_greet
* deny
    - utter_default
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Idar"}
    - slot{"location": "nagpur"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location    
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 - 700"}
    - slot{"budget": "between 300 to 700"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "average cost for two between 300 to 700"}
    - utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz.gmail.com"}
    - slot{"email": "xyz.gmail.com"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
    - slot{"email": "xyz@test.com"}
    - action_validate_email
    - slot{"email": "xyz@test.com"}
    - action_email
    - slot{"email": "xyz@test.com"}
    - utter_goodbye
    - action_restarted

## User provided incorrect cuisine
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Spanish"}
    - slot{"cuisine": "Spanish"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "> 300"}
    - slot{"budget": "> 300"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "average cost for two > 300"}
    - utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
    - slot{"email": "xyz@test.com"}
    - action_validate_email
    - slot{"email": "xyz@test.com"}
    - action_email
    - slot{"email": "xyz@test.com"}
    - utter_goodbye
    - action_restarted
    
## User provided budget which bot could not extract or understand
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* out_of_scope
    - utter_default
    - utter_ask_budget
* restaurant_search{"budget": "> 700"}
    - slot{"budget": "> 700"}
    - action_validate_budget
    - slot{"budget": "high"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "average cost for two > 700"}
    - utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
    - slot{"email": "xyz@test.com"}
    - action_validate_email
    - slot{"email": "xyz@test.com"}
    - action_email
    - slot{"email": "xyz@test.com"}
    - utter_goodbye
    - action_restarted

## User does not want the email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 300"}
    - slot{"budget": "more than 300"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "average cost for two more than 300"}
    - utter_ask_about_emailing
* deny
    - utter_goodbye
    - export

## User provided location could not be extracted or none
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Idar"}
    - slot{"location": "Idar"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}
    - slot{"budget": "between 300 to 700"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "average cost for two between 300 to 700"}
    - utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "@test.com"}
    - slot{"email": "@test.com"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
    - slot{"email": "xyz@test.com"}
    - action_validate_email
    - slot{"email": "xyz@test.com"}
    - action_email
    - slot{"email": "xyz@test.com"}
    - utter_goodbye
    - action_restarted

## User is not providing location correctly multiple times or location could not be extracted or is none
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": null}
    - slot{"location": null}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": null}
    - slot{"location": null}
    - action_validate_location
    - slot{"location": null}
    - utter_goodbye

## User providing location but not providing cuisine or it could not be extracted or is none
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "brazilian"}
    - slot{"cuisine": "brazilian"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "brazilian"}
    - slot{"cuisine": "brazilian"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_goodbye
    - action_restarted

## User providing location,cuisine but budget could not be extracted or none
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* out_of_scope
    - utter_default
    - utter_ask_budget
* out_of_scope
    - utter_default
    - utter_ask_budget
* out_of_scope
    - utter_goodbye
    - action_restarted
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Ahmedabad"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Ahmedabad"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"budget": "mid"}
    - utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "josetony78@gmail.com"}
    - slot{"email": "josetony78@gmail.com"}
    - action_validate_email
    - slot{"email": "josetony78@gmail.com"}
    - action_email
    - slot{"email": "josetony78@gmail.com"}
    - utter_ask_howcanhelp
* affirm
    - utter_goodbye
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese", "location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Mumbai"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"budget": "mid"}
    - utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "shisodianikita@gmail.com"}
    - slot{"email": "shisodianikita@gmail.com"}
    - action_validate_email
    - slot{"email": "shisodianikita@gmail.com"}
    - action_email
    - slot{"email": "shisodianikita@gmail.com"}
    - utter_ask_howcanhelp
* deny{"deny": "no thanks"}
    - utter_goodbye
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese", "location": "nagpur"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "nagpur"}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"budget": "mid"}
    - utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "josetony78@gmail.com"}
    - slot{"email": "josetony78@gmail.com"}
    - action_validate_email
    - slot{"email": "josetony78@gmail.com"}
    - action_email
    - slot{"email": "josetony78@gmail.com"}
    - utter_ask_howcanhelp
* deny{"deny": "no thanks"}
    - utter_goodbye
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese", "location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Mumbai"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"budget": "mid"}
    - utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "ppjose.abad@gmail.com"}
    - slot{"email": "ppjose.abad@gmail.com"}
    - action_validate_email
    - slot{"email": "ppjose.abad@gmail.com"}
    - action_email
    - slot{"email": "ppjose.abad@gmail.com"}
    - utter_ask_howcanhelp
* deny{"deny": "no thanks"}
    - utter_goodbye
    - action_restarted
