import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

#edit your file path
wl = pd.read_csv("C:/Users/AsadHashmi/Documents/CIC CFC/WaterLevel.csv")
mf = pd.read_csv("C:/Users/AsadHashmi/Documents/CIC CFC/MainFlows.csv")

##Import DamData and DamDataNew


class Reserve:
    
    def __init__(self, node_id,name,capacity,level,inflow,outflow,long,lat):
        
        self.node_id = node_id
        self.name = name
        self.capacity = capacity
        self.level = level
        self.inflow = inflow
        self.outflow = outflow
        self.long = long
        self.lat = lat
        
    def describe(self):
        
        #return '{} {} {} {} {} {} {} {}'.format(self.node_id,self.name,self.capacity,self.level,self.inflow,self.outflow,self.long,self.lat)
        print(self.node_id,self.name,self.capacity,self.level,self.inflow,self.outflow,self.long,self.lat)
    
    
    def rain(self,level):
        
        self.level += level
        self.describe()
        if self.level >= self.capacity * 0.9:
            print("Overflow Warning at " + self.name)
            return;
        
    def spillWay(self):    
        print(self.node_id + 1)
        return;
        

options = {
'node_color' : 'green',
'node_size' : 100,
'width' : 3,
'with_labels' : True

}

res = []
for i in range(len(mf)):
    for j in range(len(wl)):
        if(mf.iloc[:,2][i] == wl.iloc[:,2][j]):
            temp = []
            temp =  Reserve(j+1,
                            mf.iloc[:,2][i],
                            float(mf.iloc[:,3][i]),
                            float(wl.iloc[:,3][j]),
                            float(mf.iloc[:,4][i]),
                            float(mf.iloc[:,5][i]),
                            float(mf.iloc[:,12][i]),
                            float(mf.iloc[:,13][i]))
            res.append(temp)       

    
#Print Loop for all dams information
#for i in range(len(res)):
#    res[i].describe()
    

    
res[0].rain(1200)
res[0].spillWay()
    
flow=nx.DiGraph() # make a directed graph (digraph)

flow.add_nodes_from([res[0].name,res[1].name,res[2].name,res[3].name,res[4].name])

flow.add_edges_from([(res[0].name,res[1].name),
                     (res[1].name,res[2].name),
                     (res[2].name,res[3].name),
                     (res[3].name,res[4].name)],weight=1.0)




#nx.draw_shell(DG, nlist=[range(5,10), range(5)], **options)

#nx.draw_shell(flow,**options)
#plt.figure(figsize=(20,40), dpi=5)
#plt.savefig("path.png")