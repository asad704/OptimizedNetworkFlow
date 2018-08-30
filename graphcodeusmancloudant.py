
# coding: utf-8

# In[257]:


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

#edit your file path
#wl = pd.read_csv("C:/Users/MuhammadZafar/Downloads/WaterLevel.csv")
#mf = pd.read_csv("C:/Users/MuhammadZafar/Downloads/MainFlows.csv")



client = Cloudant("55a48b3d-bd73-4b30-bd83-f94f512f3796-bluemix", "5ee4b592bde6be1061b1e52f7d2e5b2af0045f590cb6820184afbac27e102021", url="https://55a48b3d-bd73-4b30-bd83-f94f512f3796-bluemix:5ee4b592bde6be1061b1e52f7d2e5b2af0045f590cb6820184afbac27e102021@55a48b3d-bd73-4b30-bd83-f94f512f3796-bluemix.cloudant.com")
client.connect()









# In[258]:


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


# In[259]:



sdata = Result(sinkdb.all_docs, include_docs=True)
mflow = Result(mainflowdb.all_docs, include_docs=True)
wlevel= Result(waterleveldb.all_docs, include_docs=True)


# In[273]:


sdata[0]


# In[260]:


def to_dict(y):
    x={}
    j=0
    for i in y:
        x[j] = i['doc']
        j= j+1
    return x


# In[261]:


sinkdata={}
mainflow ={}
waterlevel = {}


# In[262]:


sinkdata = to_dict(sdata)
mainflow =to_dict(mflow)
waterlevel = to_dict(wlevel)


# In[271]:


sinkdata


# In[240]:





# In[266]:



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
                            float(mainflow[i]['LongitudeField']),  #long
                            float(mainflow[i]['LatitudeField']),   #lat
                            float(mainflow[i]['weightField']))     #weight
                            
            res.append(temp)       

    


# In[270]:




# In[269]:


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

nx.draw_shell(flow,**options)
plt.figure(figsize=(20,40), dpi=5)
#plt.savefig("path.png")

