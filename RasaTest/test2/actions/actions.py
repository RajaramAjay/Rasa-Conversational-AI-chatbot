# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import datetime
# from weather import Weather
import requests
# class ActionGetCurrentTime(Action):
#     def name(self) -> Text:
#         return "action_get_current_time"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         message = f"The current date and time is: {current_time}"
        
#         dispatcher.utter_message(text=message)
        
#         return []


def Weather(city): 
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    url = api_address + city 
    json_data = requests.get(url).json() 
    format_add = json_data['main'] 
    print(format_add) 
    return format_add

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        city = tracker.latest_message['text']
        temp = int(Weather(city)['temp']-273)
        dispatcher.utter_template("utter_temp",tracker,temp=temp)
        return []