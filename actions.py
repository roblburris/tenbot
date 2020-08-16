from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List, Union
from rasa_sdk import Tracker
from rasa_sdk import Action
from rasa_sdk.events import UserUtteranceReverted
from tenbot_calendar import *
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from constants import *
from datetime import datetime, timedelta
import datefinder


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
            "patient_time",
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
       
        orig_date = tracker.get_slot("patient_date")
        date = find_date(orig_date)
        
        busy_times = find_busy_times(service, date)
        for time_pair in busy_times:
            dispatcher.utter_message("I'm busy from " + str(time_pair[0]) + " to " + str(time_pair[1]))
        
        return {"patient_date": orig_date}        

    
    def validate_patient_time(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
        ) -> List[Dict]:

        pat_time = tracker.get_slot(patient_time)
        name = tracker.get_slot(patient_name)
        reason = tracker.get_slot(patient_reason)
        
        schedule_appointment(service, name, time, 1.5, reason)
        return{"patient_time":pat_time}        

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:

        name = tracker.get_slot("patient_name")
        number = tracker.get_slot("patient_number")
        email = tracker.get_slot("patient_email")
        reason = tracker.get_slot("patient_reason")
        pat_time = tracker.get_slot("patient_time")

        dispatcher.utter_message("Great! Your appointmet is scheduled. Here is the info for your upcoming appointment:")
        dispatcher.utter_message("Name: " + str(name[0]))
        dispatcher.utter_message("Phone Number: " + str(number))
        dispatcher.utter_message("Email: " + str(email[0]))
        dispatcher.utter_message("Reason for Visit: " + str(reason))
        dispatcher.utter_message("Appointment Time: " + str(find_appointment(service, name, reason)['start']['dateTime'][11:16]))
        return []


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:             
        return {
            "patient_name": self.from_entity(entity="patient_name"),
            "patient_number": self.from_entity(entity="patient_number"),
            "patient_email": self.from_entity(entity="patient_email"),
            "patient_reason": [self.from_entity(entity="patient_reason"), self.from_text()],
            "patient_date": self.from_entity(entity="patient_date"),
            "patient_time": self.from_entity(entity="patient_time")
        }
    

class ActionGreetUser(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_greet", tracker)
        return [UserUtteranceReverted()]
