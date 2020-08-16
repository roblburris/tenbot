from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List, Union
from rasa_sdk import Tracker
from rasa_sdk import Action
from rasa_sdk.events import UserUtteranceReverted


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
            "patient_reason"
        ]


    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:

        dispatcher.utter_message("Thanks for getting in touch, we’ll contact you soon")
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""
        return {"use_case": self.from_text(intent="inform")}


class ActionGreetUser(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_greet", tracker)
        return [UserUtteranceReverted()]
