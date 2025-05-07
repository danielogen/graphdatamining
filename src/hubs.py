import networkx as nx
import pickle
from metrics import *
import math
from plots import *
import pandas as pd

# Load the graph
with open('data/graph/artifact_release_dependency_graph.gpickle', 'rb') as f:
    G = pickle.load(f)
# G = nx.read_gpickle("artifact_release_dependency_graph.gpickle")
print(f"Loaded Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

# Compute degrees
in_degrees = dict(G.in_degree())
out_degrees = dict(G.out_degree())
# pagerank_scores = nx.pagerank(G)

# Identify hubs (top X% in in-degree or PageRank)
hub_threshold = 0.95  # top 5%
in_degree_values = list(in_degrees.values())
degree_cutoff = sorted(in_degree_values, reverse=True)[int(len(in_degree_values) * hub_threshold)]

hubs = [n for n, d in in_degrees.items() if d >= degree_cutoff]
leaves = [n for n, d in out_degrees.items() if d == 0]

print(f"✅ Identified {len(hubs)} hub nodes (top 5% by in-degree)")
print(f"✅ Identified {len(leaves)} leaf nodes (no outgoing dependencies)")

# Optional: If you have type info, map and group
# Example: node_types = {'junit:junit': 'testing', 'slf4j:slf4j-api': 'logging', ...}
# hubs_by_type = pd.Series([node_types.get(n, 'unknown') for n in hubs]).value_counts()
# leaves_by_type = pd.Series([node_types.get(n, 'unknown') for n in leaves]).value_counts()

# --- Identify top N hubs (by in-degree) ---
top_n = 10
top_hubs = sorted(in_degrees.items(), key=lambda x: x[1], reverse=True)[:top_n]
top_hub_nodes = [n for n, _ in top_hubs]

print("✅ Top hub nodes (by in-degree):")
for n, deg in top_hubs:
    print(f"{n}: {deg} incoming edges")

# --- Identify top N prepherial (by out-degree) ---
top_peri = sorted(out_degrees.items(), key=lambda x: x[1], reverse=True)[:top_n]
top_peri_nodes = [n for n, _ in top_peri]

print("✅ Top peripheral nodes (by out-degree):")
for n, deg in top_peri:
    print(f"{n}: {deg} outgoing edges")



# --- Build subgraph: hubs + their neighbors ---
hub_neighbors = set()
for hub in top_hub_nodes:
    hub_neighbors.update(G.predecessors(hub))
    hub_neighbors.update(G.successors(hub))

subgraph_nodes = set(top_hub_nodes) | hub_neighbors
subG = G.subgraph(subgraph_nodes)

# --- Assign colors: red for hubs, blue for others ---
node_colors = ['red' if n in top_hub_nodes else 'lightblue' for n in subG.nodes]

# --- Plot ---
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(subG, seed=42)
nx.draw(subG, pos,
        with_labels=True,
        node_size=10,
        node_color=node_colors,
        edge_color='gray',
        font_size=7)

plt.title("Top Hub Nodes and Their Neighborhood")
plt.tight_layout()
plt.savefig("fig/top_hubs_subgraph.png")
plt.show()
