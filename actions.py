from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from rasa_sdk.events import AllSlotsReset
import pymysql
global results
class ActionBookSearch(Action):
	def name(self):
		return "action_book_search"

	def run(self, dispatcher:CollectingDispatcher, tracker: Tracker, domain):
		db = pymysql.connect("hostname","username","password","database_name")
		cursor = db.cursor()
		BName = tracker.get_slot('bookName')
		BEdition = tracker.get_slot('bookEdition')
		BAuthor = tracker.get_slot('bookAuthor')
		BNumber=tracker.get_slot('bookNumber')
		q = "SELECT  bnumber from detailsbook where (bname = '%s' and bedition = '%s' and bauthor= '%s');" % (BName, BEdition,BAuthor)
		try:
			cursor.execute(q)
			if cursor.execute(q)==0:
				print("Sorry, could not find any relevant data.")
			results = cursor.fetchall()
			not all(results)
			for row in results:
				avai = row[0]
				# Now print fetched result
				details = ("Availability=%s" % (avai))
				print(details)
		except:
			print ("Error: unable to fetch data")

		db.close()
		response = """The number of books currently available is {}""".format(avai)

		dispatcher.utter_message(response)
		return [SlotSet('bookNumber',BNumber)]
class ActionResetAllSlots(Action):
	def name(self):
		return "action_reset_all_slots"
	def run(self,dispatcher,tracker,domain):
		return [AllSlotsReset()]
class BookForm(FormAction):
	def name(self) -> Text:
		return "book_form"
	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		return ["bookName","bookAuthor","bookEdition"]

	def slot_mappings(self) -> Dict[Text,Any]:
		return {"bookName": self.from_entity(entity="bookName",
		                                     intent=["inform","search_provider"]),
				 "bookAuthor" : self.from_entity(entity="bookAuthor",
		 		                                intent=["inform","search_provider"]),
                 "bookEdition" :  self.from_entity(entity="bookEdition",
		 		                                intent=["inform","search_provider"])}
	def submit(self,dispatcher: CollectingDispatcher,tracker :Tracker,domain: Dict[Text,Any]) -> List[Dict]:
		return []
