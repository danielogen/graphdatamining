import pandas as pd
import networkx as nx
import pickle

df = pd.read_csv("data/csv/selected_artifact_release_dependencies.csv")  # replace with your actual file

G = nx.DiGraph()

# Add edges safely, skipping empty or NaN nodes
for _, row in df.iterrows():
    artifact_id = row['ArtifactID']
    release_id = row['ReleaseID']
    dependent_id = row['DependentArtifactID']
    
    # Check for non-NaN before adding edges
    if pd.notna(artifact_id) and pd.notna(release_id):
        G.add_edge(artifact_id, release_id)
    if pd.notna(release_id) and pd.notna(dependent_id):
        G.add_edge(release_id, dependent_id)

print(f"✅ Building graph completed: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

# Save graph as .gpickle file
with open('data/graph/artifact_release_dependency_graph.gpickle', 'wb') as f:
    pickle.dump(G, f,  pickle.HIGHEST_PROTOCOL)
