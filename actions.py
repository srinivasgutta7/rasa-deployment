# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
#
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

class loanForm(FormAction):

    def name(self):
        return "loan_form"

    @staticmethod
    def required_slots(tracker):
        return [
        "name",
        "email",
        "type_loan",
        "phone_number",
        "amount",
        ]


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any], ) -> List[Dict]:
        dispatcher.utter_message(template="utter_submit")
        return []




class ActionRespondWithUserMessage(Action):
   def name(self):
      return "action_respond_with_user_message"

   def run(self, dispatcher, tracker, domain):
      last_message = tracker.latest_message.get("text", "")
      dispatcher.utter_message(last_message)

      return []