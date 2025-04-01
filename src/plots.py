import mathplotlib as plt
import pandas as pd

df = pd.read_csv(f'output/data/out-degree-releases.csv')
plt.figure(figsize=(10, 6))
plt.scatter(df['degree'], df['frequency'], alpha=0.7)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Out-Degree (log scale)')
plt.ylabel('Frequency (log scale)')
plt.title('Out-Degree Distribution of Releases in the Maven Dependency Graph')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()