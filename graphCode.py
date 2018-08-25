import networkx as nx
import matplotlib.pyplot as plt

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
        
        return '{} {} {} {} {} {} {} {}'.format(self.node_id,self.name,self.capacity,self.level,self.inflow,self.outflow,self.long,self.lat)

        

options = {
'node_color' : 'red',
'node_size' : 500,
'width' : 3,
'with_labels' : True

}

res1 = Reserve(1,"Tarbela Dam",1500,0,249.0,120.5,38.088,72.699)
res2 = Reserve(2,"Kalabagh Dam",950,0,258.3,251.7,32.956,71.614)
res3 = Reserve(3,"Chashma Dam",950,0,318.2,300.4,32.436,71.38)
res4 = Reserve(4,"Tunsa Dam",1000,0,312.9,293.4,25.132,98.126)
res5 = Reserve(5,"Guddu",1200,0,219.9,182.9,28.392,69.772)


print(res1.describe())
print(res2.describe())
print(res3.describe())
print(res4.describe())
print(res5.describe())


flow=nx.DiGraph() # make a directed graph (digraph)

flow.add_nodes_from([res1.name,res2.name,res3.name,res4.name,res5.name])
flow.add_edges_from([(res1.name,res2.name),
                     (res2.name,res3.name),
                     (res3.name,res4.name),
                     (res4.name,res5.name)],weight=1.0)




#nx.draw_shell(DG, nlist=[range(5,10), range(5)], **options)

#nx.draw_shell(flow,**options)
#plt.figure(figsize=(20,40), dpi=5)
#plt.savefig("path.png")