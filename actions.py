from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from googletrans import Translator


from rasa_core_sdk.events import Restarted, AllSlotsReset
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import pandas as pd

import geocoder
import requests
from tabulate import tabulate

class ActionGetDataset(Action):
    def name(self):
        return 'action_get_dataset'

    def run(self, dispatcher, tracker, domain):
        keyword_en = tracker.get_slot('keyword')
        if keyword_en == "null" and len(tracker.latest_message['text'].split()) <= 3:
            keyword_en = tracker.latest_message['text'].split()[0]

        translator = Translator()
        keyword = translator.translate(keyword_en, dest='de').text
        location = tracker.get_slot('location')
        df = pd.read_csv("location.csv")
        if location == 'null':
            message = tracker.latest_message['text']
            words = message.split()
            for word in words:
                if df['Community Name'].str.contains(word, case=False).any():
                    location = word
                    [SlotSet('location', word)]
        #filled_slots=str(tracker.current_slot_values())
        try:
            g = geocoder.geonames(location, key='h1554184')
        except:
            g=''
        names = []
        links = []
        table= []
            
        if keyword != 'null' and location != 'null':
            r = requests.get('https://search.communidata.at/odgraphsearch/api/v1/get/datasets?limit=10&l=gn:'+str(g.geonames_id)+'&q='+keyword)
            response = r.json()
            if len(response['hits']['hits'])==0:
                response_bot = 'Sorry, it looks like we don\'t have that! Try to enter other keywords.'

            else:
                if len(response['hits']['hits'])>5:
                    therange = 5
                else:
                    therange = len(response['hits']['hits'])
                
                for i in range(therange):
                    name = response['hits']['hits'][i]['_source']['dataset']['dataset_name']
                    names.append(name)
                    link = response['hits']['hits'][i]['_source']['dataset']['dataset_link']
                    links.append(link)
                for i, e in zip(names,links):
                    table.append([i,e])

                response_bot = "Datasets with the keyword {} and within {}".format(keyword, location) + "                   " + tabulate(table, headers=['Name', 'Link'])


        elif keyword !='null': 
            r = requests.get('https://search.communidata.at/odgraphsearch/api/v1/get/datasets?limit=10&q='+keyword)
            response = r.json()
            if len(response['hits']['hits'])==0:
                response_bot = 'Sorry, it looks like we don\'t have that! Try to enter other keywords.'
                
            else:
                if len(response['hits']['hits'])>5:
                    therange = 5
                else:
                    therange = len(response['hits']['hits'])
                for i in range(therange):
                    name = response['hits']['hits'][i]['_source']['dataset']['dataset_name']
                    names.append(name)
                    link = response['hits']['hits'][i]['_source']['dataset']['dataset_link']
                    links.append(link)
                for i, e in zip(names,links):
                    table.append([i,e])

                response_bot = "Datasets with the keyword {}".format(keyword) + "                   " + tabulate(table, headers=['Name', 'Link'])

        elif location !='null' : 
            r = requests.get('https://search.communidata.at/odgraphsearch/api/v1/get/datasets?limit=10&l=gn:'+str(g.geonames_id))
            response = r.json()
            if len(response['hits']['hits'])==0:
                response_bot = 'Sorry, it looks like we don\'t have that! Try to enter other keywords.'
                
            else:
                if len(response['hits']['hits'])>5:
                    therange = 5
                else:
                    therange = len(response['hits']['hits'])
                for i in range(therange):
                    name = response['hits']['hits'][i]['_source']['dataset']['dataset_name']
                    names.append(name)
                    link = response['hits']['hits'][i]['_source']['dataset']['dataset_link']
                    links.append(link)
                for i, e in zip(names,links):
                    table.append([i,e])
                response_bot = "Datasets within {}".format(location) +"                   "+ tabulate(table, headers=['Name', 'Link'])

        else:     
            response_bot = 'Sorry, I don\'t understand you! .' 


        dispatcher.utter_message(response_bot)
        
        return [AllSlotsReset()]

class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 	
    def run(self, dispatcher, tracker, domain): 		
        return[AllSlotsReset()]