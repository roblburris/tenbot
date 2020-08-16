from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List, Union
from rasa_sdk import Tracker
from rasa_sdk import Action
from rasa_sdk.events import UserUtteranceReverted
from tenbot_calendar import *

service = authenticate_google()


class AppointmentScheduler(FormAction):
    """Schedules appointment"""

    def name(self):
        return "patient_appointment"

    @staticmethod
    def required_slots(tracker):
        return [
            "patient_name",
            "patient_number",
            "patient_email",
            "patient_reason",
            "patient_date",
            "patient_avail"
        ]


    def validate_patient_reason(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
        ) -> List[Dict]:
        
        name = tracker.get_slot("patient_name")
        number = tracker.get_slot("patient_number")
        email = tracker.get_slot("patient_email")
        reason = tracker.get_slot("patient_reason")

        dispatcher.utter_message("Here's what I've got so far:") 
        dispatcher.utter_message("Name: " + str(name[0]))
        dispatcher.utter_message("Phone Number: " + str(number))
        dispatcher.utter_message("Email: " + str(email[0]))
        dispatcher.utter_message("Reason for Visit: " + str(reason))
       
        return {"patient_reason": reason} 

   def validate_patient_date(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
        ) -> List[Dict]:
       
        date = tracker.get_slot("patient_date")
         


    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:

        return []


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:             
        return {
            "patient_name": self.from_entity(entity="patient_name"),
            "patient_number": self.from_entity(entity="patient_number"),
            "patient_email": self.from_entity(entity="patient_email"),
            "patient_reason": [self.from_entity(entity="patient_reason"), self.from_text()]
        }
    

class ActionGreetUser(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_greet", tracker)
        return [UserUtteranceReverted()]
