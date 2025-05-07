import networkx as nx
import pandas as pd

# --- PageRank ---
def compute_pagerank(G, weighted=False):
    if weighted:
        pr = nx.pagerank(G, weight='weight')
    else:
        pr = nx.pagerank(G)
    return pr

# --- Degree Distributions ---
def compute_degree_distributions(G):
    degrees = dict(G.degree())
    in_degrees = dict(G.in_degree()) if G.is_directed() else None
    out_degrees = dict(G.out_degree()) if G.is_directed() else None
    return degrees, in_degrees, out_degrees

# --- Clustering Coefficient ---
def compute_clustering_coefficients(G):
    undirected_G = G.to_undirected()
    local_clustering = nx.clustering(undirected_G)
    average_clustering = nx.average_clustering(undirected_G)
    return local_clustering, average_clustering

# --- Betweenness Centrality ---
def compute_betweenness_centrality(G, k=None):
    if k:
        bc = nx.betweenness_centrality(G, k=k, seed=42)
    else:
        bc = nx.betweenness_centrality(G)
    return bc

# --- Strongly Connected Components ---
def compute_strongly_connected_components(G):
    if G.is_directed():
        scc = list(nx.strongly_connected_components(G))
        scc_sizes = [len(comp) for comp in scc]
        return scc, scc_sizes
    else:
        print("⚠️ SCC only applies to directed graphs.")
        return None, None

# --- Largest Connected Component (LCC) ---
def compute_largest_connected_component(G):
    undirected_G = G.to_undirected()
    lcc = max(nx.connected_components(undirected_G), key=len)
    lcc_subgraph = G.subgraph(lcc).copy()
    return lcc_subgraph

# --- Shortest Path Lengths ---
def compute_average_shortest_path_length(G):
    if nx.is_connected(G.to_undirected()):
        avg_length = nx.average_shortest_path_length(G)
        return avg_length
    else:
        print("⚠️ Graph is disconnected; cannot compute average shortest path length.")
        return None
