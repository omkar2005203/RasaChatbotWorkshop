# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
from requests.models import Response
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="This is Hello World response !")

        return []


# weather api action

class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent=tracker.latest_message['intent']
        entity=tracker.latest_message['entities']

        print(entity)

        location=None

        for loc in entity:
            if loc['entity']=='location':
                location=loc['value']


        try:
           url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=yourKey'.format(location.lower())
           data=requests.get(url).json()
           print(data)
           
           temp_min=data['main']['temp_min']
           temp_max=data['main']['temp_max']
           overall_temp=data['main']['temp']

           dispatcher.utter_message(text='in {} max temperature is {} F and min temperature is {} F and overall temp is {}'.format(location,temp_max,temp_min,overall_temp))

        except:
            dispatcher.utter_message(text='Hey ! location not found ')


        

  

        return []





class SearchActionRestaurant(Action):

    def name(self) -> Text:
        return "action_search_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent=tracker.latest_message['intent']
        entities=tracker.latest_message['entities']
        text=tracker.latest_message['text']

        print('entities: ',entities)
        print('intent :',intent)
        print('text :',text)

        #dictTrack={'intent':intent,'entity':entities,'text':text}

        #print(dictTrack)

        for e in entities:
            if e['entity']=='resto_type' and e['value']=='indian':
                message='Go to hotel Taj'

            else:
                message='i only have list to indian restaurant'



        dispatcher.utter_message(text=message)

        return []




class ActionCovidTracker(Action):

    def name(self) -> Text:
        return "action_covid_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent=tracker.latest_message['intent']
        entities=tracker.latest_message['entities']
        text=tracker.latest_message['text']

        response=requests.get("https://api.covid19india.org/data.json").json()

        print(entities)

        state=None
        for e in entities:
            if e['entity'] == 'state_covid':
                state=e['value']
        #message='please enter correct state name'
        for data in response['statewise']:
            if data['state']==state.title():
                #print(data)
                message='There are '+data['active']+ ' active covid cases ' +' and confirmed cases are '+data['confirmed']+ ' further deaths are '+data['deaths']+ ' and delta confirmed cases are '+ data['deltaconfirmed'] +' and deaths due to delta variant are '+ data['deltadeaths'] +  ' and delta recovered number are '+data['deltarecovered']
                
                
            else:
                message='please enter correct state name'

        dispatcher.utter_message(text=message)

        return []







class ActionCountryName(Action):

    def name(self) -> Text:
        return "action_name_country"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name=tracker.get_slot('name')
        country=tracker.get_slot('country')

        # we can set slot value from here
        slotState='Maharashtra'
        message = ' your name is '+name+' and your country is '+country

        dispatcher.utter_message(text=message)
        
       #return [SlotSet("slot_name",slot_value_to_be_Set)]
        return [SlotSet("state",slotState)]




class ActionForSports(Action):

    def name(self) -> Text:
        return "action_for_sport"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="This is triggered from Actions!")

        return []
