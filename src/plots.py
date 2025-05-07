import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# ---------- Degree Distributions ----------
def plot_degree_distributions(G, bins=50):
    in_degrees = [d for n, d in G.in_degree()] if G.is_directed() else None
    out_degrees = [d for n, d in G.out_degree()] if G.is_directed() else None
    total_degrees = [d for n, d in G.degree()]

    plt.figure(figsize=(16, 4))

    # Total degree
    plt.subplot(1, 3, 1)
    plt.hist(total_degrees, bins=bins, edgecolor='black', log=True)
    plt.title("Total Degree Distribution")
    plt.xlabel("Degree")
    plt.ylabel("Frequency (log scale)")

    if in_degrees:
        # In-degree
        plt.subplot(1, 3, 2)
        plt.hist(in_degrees, bins=bins, edgecolor='black', log=True)
        plt.title("In-Degree Distribution")
        plt.xlabel("In-Degree")

        # Out-degree
        plt.subplot(1, 3, 3)
        plt.hist(out_degrees, bins=bins, edgecolor='black', log=True)
        plt.title("Out-Degree Distribution")
        plt.xlabel("Out-Degree")

    plt.tight_layout()
    plt.savefig("fig/degree_distributions.png", dpi=300)
    # plt.show()

# ---------- Top 10 PageRank Nodes with Neighbors ----------
def plot_top_pagerank_subgraph(G, pagerank_scores, top_n=10):
    top_nodes = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
    top_ids = [n for n, _ in top_nodes]
    
    # Build ego subgraph: top nodes + neighbors
    sub_nodes = set(top_ids)
    for node in top_ids:
        sub_nodes.update(G.neighbors(node))
    subG = G.subgraph(sub_nodes)

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(subG, seed=42)
    nx.draw(subG, pos, with_labels=True, node_size=500, node_color='lightblue', edge_color='gray', font_size=8)
    plt.title(f"Top {top_n} PageRank Nodes and Neighbors")
    plt.savefig(f"fig/pagerank_top_{top_n}.png", dpi=300)
    # plt.show()

# ---------- Strongly Connected Components ----------
def plot_strongly_connected_components(subG):
    # if not G.is_directed():
    #     print("⚠️ SCCs only apply to directed graphs.")
    #     return

    # sccs = list(nx.strongly_connected_components(G))
    # largest_scc = max(sccs, key=len)
    # subG = G.subgraph(largest_scc)

    # print(f"✅ Largest SCC size: {len(largest_scc)} nodes")

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(subG, seed=42)
    nx.draw(subG, pos, with_labels=True, node_size=500, node_color='lightgreen', edge_color='gray', font_size=8)
    plt.title("Largest Strongly Connected Component")
    plt.savefig("fig/largest_scc.png", dpi=300)
