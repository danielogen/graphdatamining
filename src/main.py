import networkx as nx
import pickle
from metrics import *
import math
from plots import *

# Load the graph
with open('data/graph/artifact_release_dependency_graph.gpickle', 'rb') as f:
    G = pickle.load(f)
# G = nx.read_gpickle("artifact_release_dependency_graph.gpickle")
print(f"Loaded Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

# Step 1: Identify bad nodes
bad_nodes = []
for node in G.nodes:
    if node is None or (isinstance(node, float) and math.isnan(node)):
        bad_nodes.append(node)

# Step 2: Report and remove them
if bad_nodes:
    print(f"⚠️ Found {len(bad_nodes)} invalid nodes (e.g., None or NaN). Removing...")
    G.remove_nodes_from(bad_nodes)

# Step 3: Now safely print stats
print(f"✅ Graph Loaded Successfully")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")



# Degree distributions
# deg, in_deg, out_deg = compute_degree_distributions(G)
# print("Average degree:", sum(deg.values()) / len(deg))

# PageRank
# pr = compute_pagerank(G)
# print("Top 10 PageRank nodes:", sorted(pr.items(), key=lambda x: x[1], reverse=True)[:10])

# Betweenness
bc = compute_betweenness_centrality(G, k=20)
print("Top 10 Betweenness nodes:", sorted(bc.items(), key=lambda x: x[1], reverse=True)[:10])

# Clustering - This will take alot of time.
# local_clust, avg_clust = compute_clustering_coefficients(G)
# print("Average clustering coefficient:", avg_clust)


# Strongly connected components
scc, scc_sizes = compute_strongly_connected_components(G)
if scc:
    print("Number of SCCs:", len(scc))
    print("Largest SCC size:", max(scc_sizes))

# Largest connected component
lcc_subgraph = compute_largest_connected_component(G)
print("LCC size:", lcc_subgraph.number_of_nodes())

# # Average shortest path length (if connected)
# avg_path = compute_average_shortest_path_length(lcc_subgraph)
# if avg_path:
#     print("Average shortest path length in LCC:", avg_path)


# Plot degree distributions
# plot_degree_distributions(G)

# Plot top 10 PageRank nodes with neighbors
# plot_top_pagerank_subgraph(G, pr, top_n=10)

# Plot largest strongly connected component
# plot_strongly_connected_components(lcc_subgraph)
