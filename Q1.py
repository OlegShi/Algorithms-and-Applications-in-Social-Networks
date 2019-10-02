import warnings
warnings.filterwarnings('ignore')


import networkx as nx
import matplotlib.pyplot as plt
import random
import math


#1a

def erdos_renyi(n,p):
    G = nx.Graph()
    nodes = list(x for x in range(0, n))
    for node in nodes:
        G.add_node(node);
    for node1 in nodes:
        for node2 in nodes:
            if node2>node1:
                rand = random.uniform(0,1)
                if(rand<=p):
                    G.add_edge(node1,node2)
    return G

#1b
	
def small_world(n,k,p):
    

    
    G = nx.Graph()
    nodes = list(x for x in range(0, n))
    for node in nodes:
        G.add_node(node);
        
        
    #step1
    for node in nodes:
        for d in range(1,math.floor(k/2)+1):
            G.add_edge(node,math.floor((node+d)%n))

    #step2
    
    edges_to_recreate = []
    
    #collect edges to recreate
    for e in G.edges():
        rand = random.uniform(0,1)
        if(rand<=p):
            edges_to_recreate.append(e)

    for delete in edges_to_recreate:
            G.remove_edge(delete[0],delete[1])
            #generate random different vertices to connect
            while True:
                n1=random.randint(0,n-1)
                n2 = n1
                while n1 == n2:
                    n2 = random.randint(0,n-1)
                if not G.has_edge(n1,n2):

                    G.add_edge(n1,n2)
                    break
    return G
#1c

def node_clustering_coeff(G,v):
    
    deg = G.degree(v)
    
    if deg <= 1:
        return 0
    
    count = 0
    for u1 in G.neighbors(v):
        for u2 in G.neighbors(v):
            if G.has_edge(u1,u2):
                count+=1

    return count/(deg*(deg-1))



def graph_clustering_coeff(G):
    count = 0
    for v in G.nodes():
        count += node_clustering_coeff(G,v) 
    deg = G.degree(v)
    return count/G.number_of_nodes()
	
	
#1d

def degree_distribution(G):
    degree_dist = {}
    for node in G.nodes():
        node_degree = G.degree(node)
        if node_degree not in degree_dist:
            degree_dist[node_degree] = 0
        degree_dist[node_degree] += 1
    return degree_dist

def print_graph_data(G):
    print("diameter:" + str(nx.diameter(G)))
    degree_dist = degree_distribution(G)
    print("degree distribution:")
    plt.bar(list(degree_dist.keys()), degree_dist.values(), color='g')
    plt.show()
    print("clustering coefficient:" + str(graph_clustering_coeff(G)))


def run_test():
    print("erdos renyi model")
    print_graph_data(erdos_renyi(1000,0.2))

    print("*********")
    print("small world model")
    print_graph_data(small_world(1000, 8, 0.1))
