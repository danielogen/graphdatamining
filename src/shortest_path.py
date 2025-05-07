import networkx as nx
import pickle
from metrics import *
import math
from plots import *
import pandas as pd
import matplotlib.pyplot as plt

# Load the graph
with open('data/graph/artifact_release_dependency_graph.gpickle', 'rb') as f:
    G = pickle.load(f)
# G = nx.read_gpickle("artifact_release_dependency_graph.gpickle")
print(f"Loaded Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

if nx.is_connected(G.to_undirected()):
    print("✅ The graph is fully connected (ignoring direction)")
else:
    print("⚠️ The graph is disconnected; we will analyze the largest connected component (LCC)")

if nx.is_strongly_connected(G):
    avg_length = nx.average_shortest_path_length(G)
    print(f"✅ Average shortest path length (directed): {avg_length:.2f}")
else:
    print("⚠️ Graph is not strongly connected. We’ll analyze the largest SCC")

    # Extract largest SCC
    scc_nodes = max(nx.strongly_connected_components(G), key=len)
    scc_subgraph = G.subgraph(scc_nodes).copy()

    avg_length = nx.average_shortest_path_length(scc_subgraph)
    print(f"✅ Average shortest path length in largest SCC: {avg_length:.2f}")
