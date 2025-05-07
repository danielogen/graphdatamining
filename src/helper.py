import pandas as pd

# Load your artifacts CSV (adjust the path as needed)
csv_path = 'data/csvtop_5000_artifacts.csv'
df = pd.read_csv(csv_path)

# Extract the artifactId column
artifact_ids = df['artifactId'].dropna().unique()

# Format as a Cypher IN list
cypher_in_list = "[" + ", ".join(f"'{aid}'" for aid in artifact_ids) + "]"

# Output the Cypher-ready list
print("Copy and paste this into your Cypher query WHERE clause:")
print(f"a.id IN {cypher_in_list}") 
# Define output file
output_file = 'cypher_in_list.txt'

# Write to file
with open(output_file, 'w') as f:
    f.write(f"a.id IN {cypher_in_list}\n")

print(f"✅ Cypher IN list written to {output_file}")