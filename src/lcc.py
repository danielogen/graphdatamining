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

# --- Load your graph ---
# G = nx.read_gpickle("artifact_dependency_graph.gpickle")
undirected_G = G.to_undirected()

# --- Compute connected components ---
components = list(nx.connected_components(undirected_G))
component_sizes = [len(c) for c in components]
num_components = len(components)
largest_component_size = max(component_sizes)
total_nodes = G.number_of_nodes()

# --- Report stats ---
print(f"✅ Total connected components: {num_components}")
print(f"✅ Largest connected component (LCC) size: {largest_component_size} nodes")
print(f"✅ Total nodes in graph: {total_nodes}")

lcc_percentage = (largest_component_size / total_nodes) * 100
print(f"✅ LCC covers {lcc_percentage:.2f}% of all nodes")

small_components = [size for size in component_sizes if size < largest_component_size]
small_component_percentage = (sum(small_components) / total_nodes) * 100
print(f"✅ Small components cover {small_component_percentage:.2f}% of all nodes")

# --- Plot component size distribution ---
plt.figure(figsize=(10, 6))
plt.hist(component_sizes, bins=50, edgecolor='black', log=True)
plt.title("Connected Component Size Distribution")
plt.xlabel("Component Size (number of nodes)")
plt.ylabel("Frequency (log scale)")
plt.tight_layout()
plt.savefig("fig/component_size_distribution.png", dpi=300)
plt.show()
