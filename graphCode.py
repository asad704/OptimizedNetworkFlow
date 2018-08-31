

print("Loading...")

import requests

from cloudant.client import Cloudant

from cloudant.error import CloudantException

from cloudant.result import Result, ResultByKey, QueryResult

import pandas as pd

from pandas import DataFrame, read_csv

import numpy as np

import json

from cloudant.query import Query

from cloudant.database import CloudantDatabase

import networkx as nx

import matplotlib.pyplot as plt

import pandas as pd

from datetime import datetime
from cloudant.client import Cloudant
import pandas as pd



#edit your file path

#wl = pd.read_csv("C:/Users/MuhammadZafar/Downloads/WaterLevel.csv")

#mf = pd.read_csv("C:/Users/MuhammadZafar/Downloads/MainFlows.csv")




# credentials
username = "55a48b3d-bd73-4b30-bd83-f94f512f3796-bluemix"
password = "5ee4b592bde6be1061b1e52f7d2e5b2af0045f590cb6820184afbac27e102021"
urls = "https://" + username + ":" + password + "@" + username + ".cloudant.com"

client = Cloudant(username, password, url=urls)
client.connect()
print("Cloudant Connected!")
# Open an existing database
db_name = ['mainflow','waterlevel','sink']
mainflowtemp = client[db_name[0]]
waterleveltemp = client[db_name[1]]
sinktemp = client[db_name[2]]

save_file = False 


class Reserve:

    

    def __init__(self, node_id,name,capacity,level,inflow,inflow_cap,outflow,outflow_cap,long,lat,weight):

        

        self.node_id = node_id

        self.name = name

        self.capacity = capacity

        self.level = level

        self.inflow = inflow

        self.inflow_cap = inflow_cap

        self.outflow = outflow

        self.outflow_cap = outflow_cap

        self.long = long

        self.lat = lat

        self.weight = weight

        

    def describe(self):

        

        print(self.node_id,self.name,self.capacity,self.level,self.inflow,self.inflow_cap,self.outflow,self.outflow_cap,self.long,self.lat)

    

    

    def rain(self,level): 

        self.level += level

        self.describe()

        if self.level >= self.capacity * 0.9:

            print("Overflow Warning at " + self.name)

            self.checkCap(res);

            return;

        
    def checkCap(self,res):    

        if res[self.node_id].level <= res[self.node_id].capacity * 0.5:

            print("Moving water to " + res[self.node_id].name)

            self.level -= 300

            res[self.node_id].level += 300

            self.describe()

            res[self.node_id].describe()

            return;

       
options = {

'node_color' : 'green',

'node_size' : 100,

'width' : 3,

'with_labels' : True



}

#weather API
def get_weather(lat,long):
    username = '5deff39b-b3ba-4731-a0f3-ee1ee2352868'
    password = 'tW04Lpv1CE'
    watsonUrl = 'https://twcservice.au-syd.mybluemix.net/api/weather/v1/geocode/{}/{}/forecast/hourly/48hour.json'.format(lat,long)
 
    try:
        r = requests.get(watsonUrl,auth=(username,password))
        return r.text
    except:
        return False
    
    
def display_weather(results):
    data = {}
    i =0
    for x in results['forecasts']:
        i = i + 1
        data[i] = [x['pop'],x['qpf'],x['severity'],x['phrase_32char']]
    return data





def to_dict(y):
    data = {}
    for ind, document in enumerate(y):
        one_doc = dict(document)
        data[ind]= one_doc
    return data

mainflow ={}
waterlevel = {}
sink = {}


sink = to_dict(sinktemp)
mainflow =to_dict(mainflowtemp)
waterlevel = to_dict(waterleveltemp)







res = []

for i in range(len(mainflow)):

    for j in range(len(waterlevel)):

        if(mainflow[i]['NodeField'] == waterlevel[j]['Namefield']):

            temp = []

            temp =  Reserve(j+1,                     #node_id

                            mainflow[i]['NodeField'], #name

                            float(mainflow[i]['CapacityField']),  #capacity

                            float(waterlevel[j]['WaterLevelfield']),  #level

                            float(mainflow[i]['In FlowField']), #inflow

                            350,  #outflow cap

                            float(mainflow[i]['OutFlowField']),  #outflow

                            350,      #outflow cap

                            float(mainflow[i]['LongitudeField']),  

                            float(mainflow[i]['LatitudeField']),   

                            float(mainflow[i]['weightField']))     #weight

                            

            res.append(temp)       

            
#Print Loop for all dams information

for i in range(len(res)):

    res[i].describe()

    



    

res[1].rain(1200)

res[0].describe()



    

flow=nx.DiGraph() # make a directed graph (digraph)



flow.add_nodes_from([res[0].name,res[1].name,res[2].name,res[3].name,res[4].name])



flow.add_edges_from([(res[0].name,res[1].name),

                     (res[1].name,res[2].name),

                     (res[2].name,res[3].name),

                     (res[3].name,res[4].name)])









#nx.draw_shell(DG, nlist=[range(5,10), range(5)], **options)

#weather data retrieval
weather = {}
results = []
resultstemp = []
for i in range(len(mainflow)):
    long = round(float(mainflow[i]['LongitudeField']),3)
    lat  = round(float(mainflow[i]['LatitudeField']),3)
    results.append(get_weather(lat, long))
        
    if results[i] != False:
        resultstemp.append(json.loads(str(results[i])))
        print(mainflow[i]['NodeField'])
        weather[mainflow[i]['NodeField']] =  display_weather(resultstemp[i])            
    else:
        print('Something went wrong :-(') 


nx.draw_shell(flow,**options)

plt.figure(figsize=(20,40), dpi=5)

plt.savefig("path.png")

