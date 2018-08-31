from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import pandas as pd
from pandas import DataFrame, read_csv
import numpy

client = Cloudant("55a48b3d-bd73-4b30-bd83-f94f512f3796-bluemix", "5ee4b592bde6be1061b1e52f7d2e5b2af0045f590cb6820184afbac27e102021", url="https://55a48b3d-bd73-4b30-bd83-f94f512f3796-bluemix:5ee4b592bde6be1061b1e52f7d2e5b2af0045f590cb6820184afbac27e102021@55a48b3d-bd73-4b30-bd83-f94f512f3796-bluemix.cloudant.com")
client.connect()


#for mainflow database
databaseName = "mainflow"
mainflowdb = client.create_database(databaseName)

if mainflowdb.exists():
    print("{0} successfully created.\n".format(databaseName))


df = read_csv(r"C:\Users\UmerFarooq\Desktop\Umer Farooq2_z63fm75v\CallForCode\IBMCloudant\csv\MainFlows.csv")
mainflow=df.values
mainflow
for document in mainflow:
_id = document[0]
    RowID = document[1]
    NodeID = document[2]
    Node = document[3]
    Capacity = document[4]
    Inflow= document[5]
    Outflow = document[6]
    Flow = document[7]
    Dam =document[8]
    Cannal= document[9]
    Barrage= document[10]
    Field= document[11]
    Merger= document[12]
    Latitude= document[13]
    Longitude=document[14]
    ConnectedFrom = document[15]
    ConnectedTo= document[16]
    StartNode= document[17]
    SinkNode= document[18]
    Weight= document[19]
    
    jsonDocument = {
        "_id":str(_id),
        "RowIDField":RowID,
        "NodeIDField":NodeID,
        "NodeField":Node,
        "CapacityField":Capacity,
        "In FlowField":Inflow,
        "OutFlowField":Outflow,
        "FlowField":Flow,
        "DamField":Dam,
        "CannalField":Cannal,
        "BarrageField":Barrage,
        "FieldField":Field,
        "MergerField":Merger ,
        "LatitudeField":Latitude,
        "LongitudeField":Longitude,
        "ConnectedFromField":ConnectedFrom,
        "ConnectedToField":ConnectedTo,
        "StartNodeField":StartNode,
        "SinkNodeField":SinkNode,
        "weightField":Weight
     }

    
    newDocument = mainflowdb.create_document(jsonDocument)

    if newDocument.exists():
        print("Successful document created",document)


#for WaterLevel database
databaseName = "waterlevel"
waterleveldb = client.create_database(databaseName)

if waterleveldb.exists():
    print("{0} successfully created.\n".format(databaseName))


df = read_csv(r"C:\Users\UmerFarooq\Desktop\Umer Farooq2_z63fm75v\CallForCode\IBMCloudant\csv\WaterLevel.csv")
waterlevel=df.values
print(waterlevel)

for document in waterlevel:
    _id = document[0]
    RowID=document[1]
    Node=document[2]
    Name=document[3]
    WaterLevel=document[4]

    
    jsonDocument = {
    '_id':str(_id),
    'RowIDfield':RowID,
    'Nodefield':Node,
    'Namefield':Name,
    'WaterLevelfield':WaterLevel



    }
    newDocument = waterleveldb.create_document(jsonDocument)

    if newDocument.exists():
        print("Successful document created",document)


#For Sink database
databaseName = "sink"
sinkdb = client.create_database(databaseName)

if sinkdb.exists():
    print("{0} successfully created.\n".format(databaseName))


df = read_csv(r"C:\Users\UmerFarooq\Desktop\Umer Farooq2_z63fm75v\CallForCode\IBMCloudant\csv\Sink.csv")
sink=df.values
print(sink)

for document in sink:
     _id = document[0]
    RowID=document[1]
    Node=document[2]
    Sink=document[3]
    Population=document[4]
    IndustrailLandProvided=document[5]
    MaximunCapacity=document[6]

    
    jsonDocument = {
    '_id' : str(_id),
    'RowIDfield':RowID,
    'Nodefield':Node,
    'Sinkfield':Sink,
    'Populationfield':Population,
    'IndustrailLandProvidedfield':IndustrailLandProvided,
    'MaximunCapacityfield':MaximunCapacity


    }
    newDocument = sinkdb.create_document(jsonDocument)

    if newDocument.exists():
        print("Successful document created",document)

#For Weight database
databaseName = "weight"
weightdb = client.create_database(databaseName)

if weightdb.exists():
    print("{0} successfully created.\n".format(databaseName))


df = read_csv(r"C:\Users\UmerFarooq\Desktop\Umer Farooq2_z63fm75v\CallForCode\IBMCloudant\csv\Weights.csv")
weight=df.values
print(weight)

for document in weight:
    RowID=document[0]
    NodeA=document[1]
    NodeB=document[2]
    Weight=document[3]

    
    jsonDocument = {
    'RowIDfield':RowID,
    'NodeAfield':NodeA,
    'NodeBfield':NodeB,
    'Weightfield':Weight

    }
    newDocument = weightdb.create_document(jsonDocument)

    if newDocument.exists():
        print("Successful document created",document)






