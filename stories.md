
## explore1             
* greet
  - utter_greet
  - utter_search_or_explore
* explore               
  - utter_give_choice_keyword
* giving_keyword {"keyword": "animals"}
  - slot {"keyword": "animals"}
  - utter_give_choice_location
* giving_location {"location": "Vienna"}
  - slot {"location": "Vienna"}
  - action_get_dataset
> further_dialogue

## explore2
* greet
  - utter_greet
  - utter_search_or_explore           
* explore               
  - utter_give_choice_keyword
* giving_keyword {"keyword": "buildings"}
  - slot {"keyword": "buildings"}
  - utter_give_choice_location
* giving_location {"location": "graz"}
  - slot {"location": "graz"}
  - action_get_dataset
> further_dialogue



## explore3 
* greet         
  - utter_greet
  - utter_search_or_explore
* explore  
  - utter_give_choice_keyword
* giving_keyword {"keyword": "education"}
  - slot {"keyword": "education"}
  - utter_give_choice_location
* giving_location {"location": "salzburg"}
  - slot {"location": "salzburg"}
  - action_get_dataset
> further_dialogue


## explore_to_search
* greet          
  - utter_greet
  - utter_search_or_explore
* explore  
  - utter_give_choice_keyword
* giving_keyword {"keyword": "health care"}
  - slot {"keyword": "health_care"}
  - utter_give_choice_location
* giving_location {"location": "innsbruck"}
  - slot {"location": "innsbruck"}
  - action_get_dataset
> further_dialogue

## 1
> further_dialogue
* search {"keyword": "Vienna"}
  - slot {"keyword": "Vienna"}
  - action_get_dataset
> further_dialogue
  
## 3
> further_dialogue
* search
  - utter_ask_keyword
* search {"keyword": "Austria"}
  - slot {"keyword": "Austria"}
  - action_get_dataset
> further_dialogue

## search_to_explore 
> further_dialogue
* greet         
  - utter_greet
  - utter_search_or_explore
* search
   - utter_ask_keyword
* search {"keyword": "Austria"}
  - slot {"keyword": "Austria"}
  - action_get_dataset
> further_dialogue

## further_dialogue_1
> further_dialogue
* explore   
  - utter_give_choice_keyword
* giving_keyword {"keyword": "military"}
  - slot {"keyword": "military"}
  - utter_give_choice_location
* giving_location
  - action_get_dataset
> further_dialogue


## search1
* greet
  - utter_greet
  - utter_search_or_explore
* search {"keyword": "Austria"}
  - slot {"keyword": "Austria"}
  - action_get_dataset
> further_dialogue


##search2
* greet
  - utter_greet
  - utter_search_or_explore
* search
  - utter_ask_keyword
* search {"keyword": "Austria"}
  - slot {"keyword": "Austria"}
  - action_get_dataset
> further_dialogue


## user affirms question
> check_asked_question
* affirm
  - utter_happy
> further_dialogue
  
## user denies question
> check_asked_question
* deny
  - utter_handle_denial
> further_dialogue

## thanks
> further_dialogue
* thanks
  - utter_did_that_help
> check_asked_question

## goodbye
> further_dialogue
* goodbye
  - utter_goodbye
> further_dialogue