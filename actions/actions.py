# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from matplotlib.pyplot import text

from rasa_sdk import Action, Tracker
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from database_connectivity import DataUpdate, GetData
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "submit_insurance_form"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []
class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_insurance_form"

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        
        if len(slot_value) == 0:
            dispatcher.utter_message(text="Enter a valid Name the name is empty")
            return {"name": None}
        return {"name": slot_value}
    
    def validate_registration_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        
        if len(slot_value) == 0:
            dispatcher.utter_message(text="That must've been a typo.")
            return {"registration_date": None}
        return {"registration_date": slot_value}

    
    def validate_driving_license(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:


        # If the name is super short, it might be wrong.

        if len(slot_value) == 0:
            dispatcher.utter_message(text="That must've been a typo.")
            return {"driving_license": None}
        return {"driving_license": slot_value}
    
    
    def validate_license_plate(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        

        # If the name is super short, it might be wrong.
        
        if len(slot_value) == 0:
            dispatcher.utter_message(text="Enter a valid license plate number")
            return {"license_plate": None}
        return {"license_plate": slot_value}

    
    def validate_types(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        
        if len(slot_value) == 0:
            dispatcher.utter_message(text="Enter a valid type")
            return {"types": None}
        return {"types": slot_value}

class ValidateForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_check_form"

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        
        if len(slot_value) == 0:
            dispatcher.utter_message(text="Enter a valid Name the name is empty")
            return {"name": None}
        return {"name": slot_value}
    

    
    def validate_license_plate(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        

        # If the name is super short, it might be wrong.
        
        if len(slot_value) == 0:
            dispatcher.utter_message(text="Enter a valid license plate number")
            return {"license_plate": None}
        return {"license_plate": slot_value}

    



class ActionWorld(Action):

    def name(self) -> Text:
        return "submit_check_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        (types,price,expiry_date)=GetData(tracker.get_slot("license_plate"))
        
        dispatcher.utter_message(text="Your current plan is {0},the price of it is {1} and it will expire on {2}".format(types,price,expiry_date))
        return []


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "submit_insurance_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        if(tracker.get_slot("types")=="Comprehensive"):
            DataUpdate(tracker.get_slot("name"),tracker.get_slot("registration_date"),tracker.get_slot("driving_license"),tracker.get_slot("license_plate"),tracker.get_slot("types"),500)
        elif (tracker.get_slot("types")=="Standalone Own"):
            DataUpdate(tracker.get_slot("name"),tracker.get_slot("registration_date"),tracker.get_slot("driving_license"),tracker.get_slot("license_plate"),tracker.get_slot("types"),300)
        elif (tracker.get_slot("types")=="Standalone Third-party"):
            DataUpdate(tracker.get_slot("name"),tracker.get_slot("registration_date"),tracker.get_slot("driving_license"),tracker.get_slot("license_plate"),tracker.get_slot("types"),150)
        
        (types,price,expiry_date)=GetData(tracker.get_slot("license_plate"))
        dispatcher.utter_message(text="Thank you for purchasing your plan will expire on {0}".format(expiry_date))
        

        return []