import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import networkx as nx
import random

def check_balance(G):

    posEdges = [(u,v) for (u,v,d) in G.edges(data=True) if d['label'] =='+'] 
    negEdges=[(u,v) for (u,v,d) in G.edges(data=True) if d['label'] == '-'] 

    Hpos = nx.Graph()
    Hneg = nx.Graph()
   
    #creats graph from postivie edges
    Hpos.add_edges_from(posEdges)

    #creats graph from negative edges
    Hneg.add_edges_from(negEdges)
    
     #validates that none of the positive edges components contains negetive edge
    for comp in nx.connected_components(Hpos):
        for edge in negEdges:
            if edge[0] in comp and edge[1] in comp:
                return False

    #directed representation of the graph
    dGraph = Hpos.to_directed()
    
    #super node for each component
    cG = nx.condensation(dGraph)
    
    #extract mapping
    mapping = cG.graph['mapping']

    T = cG.copy()
    
    #Connect components A and B if there is negative edge between the members
    for n1 in mapping.items():
        for n2 in mapping.items():
            for edge in negEdges:
                if edge[0] == n1[0] and edge[1] == n2[0]:
                    T.add_edge(n1[1],n2[1])
                    
    #counter for unique node's generator
    counter = len(G.node())
    #adds isolated nodes as components( nodes with negative edges only in the original graph  )
    for node in Hneg.nodes():
        flag = False
        for m in mapping.items():
            if node == m[0]:
                flag = True
                break
        if flag == False :  
            T.add_node(counter)
            for edge in negEdges:
                print(edge)
                for d in mapping.items():
                    if (edge[0] == node and  edge[1] == d[0]) or (edge[1] == node and  edge[0] == d[0]) :
                        T.add_edge(counter, d[1])
            counter += 1    
    
    #back to unirected representation of the graph                      
    T = T.to_undirected()       
    
    #simulates two-coloring
    color={}
    for n in T: 
        if n in color: continue
        queue=[n]  
        color[n]=1 # nodes seen with color (1 or 0)
        while queue:
            v=queue.pop()
            c=1-color[v] # opposite color of node v
            for w in T[v]:
                if w in color: 
                    if color[w]==color[v] and w!=v:
                        return False
                else:
                    color[w]=c
                    queue.append(w)
    return True

