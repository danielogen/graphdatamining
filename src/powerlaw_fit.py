import networkx as nx
import powerlaw
import matplotlib.pyplot as plt
import pickle
# Load your graph
# G = nx.read_gpickle("artifact_release_dependency_graph_top10_bfs10k.gpickle")
# Load the graph
with open('data/graph/artifact_release_dependency_graph.gpickle', 'rb') as f:
    G = pickle.load(f)
# G = nx.read_gpickle("artifact_release_dependency_graph.gpickle")
print(f"Graph loaded: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

# Get total degree sequence
degree_sequence = [d for n, d in G.degree()]
degree_sequence = [d for d in degree_sequence if d > 0]  # remove zeros (optional)

# Fit the power-law
fit = powerlaw.Fit(degree_sequence, discrete=True)
print(f"Power-law alpha (slope): {fit.power_law.alpha:.4f}")
print(f"Power-law xmin (cutoff): {fit.power_law.xmin}")

# Compare power-law vs. other distributions
R, p = fit.distribution_compare('power_law', 'lognormal')
print(f"Comparison: R = {R:.4f}, p = {p:.4f}")
if R > 0 and p < 0.05:
    print("✅ Power-law is a better fit (significant)")
else:
    print("⚠️ Power-law may not be the best fit")


# Plot empirical data + fitted power-law
plt.figure(figsize=(8, 6))
fit.plot_pdf(color='b', linewidth=2, label='Empirical data')
fit.power_law.plot_pdf(color='r', linestyle='--', label='Fitted power-law')

plt.title("Degree Distribution with Power-Law Fit")
plt.xlabel("Degree")
plt.ylabel("Probability")
plt.legend()
plt.grid(True, which='both', ls='--')
plt.tight_layout()
plt.savefig("fig/powerlaw_fit.png", dpi=300)
plt.show()