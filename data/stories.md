## search book happy path
* greet
  - utter_greet
* usergreet
  - utter_response_greet
* inform{"bookName":"java"}
  - book_form
  - slot{"bookName":"java"}
  - slot{"bookAuthor":"hermen schildt"}
  - slot{"bookEdition":"9th edition"}
  - form{"name": "book_form"}
  - form{"name":null}
  - action_book_search
  - slot{"bookNumber":"100"}
* search_provider{"bookName":"java","bookAuthor":"Herbert Schildt","bookEdition":"9th edition"}
  - action_book_search
  - slot{"bookNumber":"150"}
  - action_reset_all_slots
* search_provider{"bookName":"java"}
  - book_form
  - slot{"bookName":"java"}
  - slot{"bookAuthor":"hermen schildt"}
  - slot{"bookEdition":"9th edition"}
  - form{"name": "book_form"}
  - form{"name":null}
  - action_book_search
  - slot{"bookNumber":"150"}
  - action_reset_all_slots
* thanks
  - utter_welcome

##search book happy path2
* greet
  - utter_greet
* usergreet
  - utter_response_greet
* search_provider{"bookName":"java","bookAuthor":"Herbert Schildt","bookEdition":"9th edition"}
  - action_book_search
  - slot{"bookNumber":"150"}
  - action_reset_all_slots
* thanks
  - utter_welcome

##search book happy path2
* greet
  - utter_greet
* usergreet
  - utter_response_greet
* search_provider{"bookName":"java"}
  - book_form
  - slot{"bookName":"java"}
  - slot{"bookAuthor":"hermen schildt"}
  - slot{"bookEdition":"9th edition"}
  - form{"name": "book_form"}
  - form{"name":null}
  - action_book_search
  - slot{"bookNumber":"150"}
  - action_reset_all_slots
* thanks
  - utter_welcome

##search book multiple requests
* greet
  - utter_greet
* usergreet
  - utter_response_greet
* search_provider{"bookName": "java"}
  - book_form
  - slot{"bookName":"java"}
  - slot{"bookAuthor":"hermen schildt"}
  - slot{"bookEdition":"9th edition"}
  - form{"name": "book_form"}
  - form{"name":null}
  - action_book_search
  - slot{"bookNumber":"150"}
  - action_reset_all_slots
* inform{"bookName":"Java"}
  - book_form
  - slot{"bookName":"java"}
  - slot{"bookAuthor":"hermen schildt"}
  - slot{"bookEdition":"9th edition"}
  - form{"name": "book_form"}
  - form{"name":null}
  - action_book_search
  - slot{"bookNumber":"150"}
  - action_reset_all_slots
* search_provider{"bookName": "java"}
  - book_form
  - slot{"bookName":"java"}
  - slot{"bookAuthor":"hermen schildt"}
  - slot{"bookEdition":"9th edition"}
  - form{"name": "book_form"}
  - form{"name":null}
  - action_book_search
  - slot{"bookNumber":"150"}
  - action_reset_all_slots
* thanks
  - utter_welcome

##direct search inform->search_provider
* inform{"bookName":"Java"}
  - book_form
  - slot{"bookName":"java"}
  - slot{"bookAuthor":"hermen schildt"}
  - slot{"bookEdition":"9th edition"}
  - form{"name": "book_form"}
  - form{"name":null}
  - action_book_search
  - slot{"bookNumber":"150"}
  - action_reset_all_slots
* search_provider{"bookName": "java"}
  - book_form
  - slot{"bookName":"java"}
  - slot{"bookAuthor":"hermen schildt"}
  - slot{"bookEdition":"9th edition"}
  - form{"name": "book_form"}
  - form{"name":null}
  - action_book_search
  - slot{"bookNumber":"150"}
  - action_reset_all_slots

##direct search search_provider->inform
* search_provider{"bookName": "java"}
  - book_form
  - slot{"bookName":"java"}
  - slot{"bookAuthor":"hermen schildt"}
  - slot{"bookEdition":"9th edition"}
  - form{"name": "book_form"}
  - form{"name":null}
  - action_book_search
  - slot{"bookNumber":"150"}
  - action_reset_all_slots
* inform{"bookName":"Java"}
  - book_form
  - slot{"bookName":"java"}
  - slot{"bookAuthor":"hermen schildt"}
  - slot{"bookEdition":"9th edition"}
  - form{"name": "book_form"}
  - form{"name":null}
  - action_book_search
  - slot{"bookNumber":"150"}
  - action_reset_all_slots

##greet
* greet
  - utter_greet

##thanks
* thanks
  - utter_welcome

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## bot out-of-scope
* out_of_scope
  - utter_default
* out_of_scope
  - utter_default
* out_of_scope
  - utter_help_message

## love and deny
 * love
  - utter_denial

##appreciate
 * appreciate
  - utter_thank
