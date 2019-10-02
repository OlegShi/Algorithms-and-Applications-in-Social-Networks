import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import networkx as nx
import math

def degree_centrality(G):

    centrality_list = {}
    num_of_nodes=len(G.nodes());
    for node in G.nodes():
        node_degree = len(list(G.neighbors(node)))
        node_cent=(node_degree)/(num_of_nodes-1)
        centrality_list.update({node:node_cent})
    
    return(centrality_list)

############################

def closeness_centrality(G):

    centrality_list = {}
    num_of_nodes=len(G.nodes());
    
    for node in G.nodes():
        d_sum=0
        for n in G.nodes():
            d=nx.shortest_path_length(G, node, n, weight=None)
            d_sum=d_sum+d
            
        node_cent=(1/d_sum)*(num_of_nodes-1)
        centrality_list.update({node:node_cent})
    
    return(centrality_list)

############################

def betweenness_centrality(G):

    centrality = {}

    for node in G.nodes():
        centrality[node] = 0;
        
    for s in G.nodes():
        for t in G.nodes:
            if s==t:
                continue
                
            paths =  nx.all_shortest_paths(G, s, t)
            num_of_paths=0
            for path in paths:
                num_of_paths += 1
                
            paths =  nx.all_shortest_paths(G, s, t)
            for p in paths:
                for i in range(0,len(p)):
                    
                    if p[i] == s or p[i] == t:
                        continue
                        
                    centrality[p[i]] += 1/num_of_paths
                               
    num_of_nodes=len(G.nodes())
    
    if(num_of_nodes > 2):
        #normalize
        for n in centrality:
            centrality[n] = (centrality[n])/((num_of_nodes-1)*(num_of_nodes-2))
    
    return centrality
