## Understanding Software Ecosystem Dependencies: Structural and Connectivity Analysis of Maven Central
## Abstract (Short)
Understanding the structural characteristics and connectivity patterns of large-scale software ecosystems is critical for enhancing software reuse, improving ecosystem resilience, and mitigating security risks. In this study, we investigate the Maven Central ecosystem, one of the largest repositories of Java libraries, by applying network science techniques to its dependency graph. Leveraging the Goblin framework, we extracted a sample consisting of the top 5,000 most connected libraries. This sampling strategy resulted in a curated graph comprising approximately 1.3 million nodes and 20.9 million edges.

---

## Project Structure

```
graphdatamining-main/
├── .gitignore                # Git ignore rules
├── LICENSE                   # Project license (MIT)
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── src/                      # Main source code
│   ├── build_graph.py            # Builds the dependency graph from data
│   ├── demo.ipynb                # Interactive Jupyter notebook demonstrating key features
│   ├── helper.py                 # Utility functions
│   ├── hubs.py                   # Analysis of graph hubs
│   ├── lcc.py                    # Analysis of Largest Connected Component (LCC)
│   ├── main.py                   # Main orchestration script
│   ├── metrics.py                # Network metrics computation
│   ├── plots.py                  # Visualization utilities
│   ├── powerlaw_fit.py           # Power-law fitting on graph data
│   ├── shortest_path.py          # Shortest path analysis
│   ├── cypher-scripts/           # Neo4j Cypher scripts for graph export & querying
│   │   ├── export-csv-artifacts-releases-depency
│   │   ├── in-degree-libraries
│   │   ├── load-csv
│   │   ├── out-degree-releases
│   │   └── top-50-highly-connencted
│   ├── data/                     # Data folder (preloaded CSVs and graphs)
│   │   ├── csv/
│   │   │   ├── .gitkeep
│   │   │   ├── in-degree-libraries.csv
│   │   │   ├── out-degree-releases.csv
│   │   │   └── top_5000_artifacts.csv
│   │   └── graph/
│   │       └── .gitkeep
│   └── fig/                      # Figures and plots generated
│       ├── component_size_distribution.png
│       ├── degree_distribution-all.png
│       ├── degree_distributions.png
│       ├── pagerank_top_10.png
│       ├── powerlaw_fit.png
```

---

## Usage Instructions

### Prerequisites

* Python 3.8+
* Neo4j (optional, for Cypher querying)

### Installation

```bash
# Clone the repository
git clone https://github.com/danielogen/graphdatamining.git
cd graphdatamining

# Install required packages
pip install -r requirements.txt
```
--- 
### About the dataset
The dataset used for this project is available at: [https://zenodo.org/records/13734581](https://zenodo.org/records/13734581). Due to its large size, we were unable to upload the entire dataset. However, to support the testing of certain scripts, we have provided **sample datasets** specifically for computing **in-degree** and **out-degree** for libraries and releases, respectively. You can find these sample datasets in the following directory: `src/data/csv`

---

### Running the code
#### Interactive Notebook - Reproducing the results
This is the easiest approach to reproduce the results presented in the paper. In the ``src`` directory, simply run the demo.ipynb file.


```bash
python src/main.py
```

This script orchestrates the entire pipeline: data loading, graph construction, metric computation, and visualization.

---

## Features

* **Graph Construction**: Build artifact-release dependency graph from CSV data.
* **Metrics Analysis**:

  * Degree distribution
  * In-degree and out-degree analysis
  * PageRank computation
  * Hub detection
  * Largest Connected Component (LCC) analysis
  * Shortest path metrics
* **Visualization**:

  * Degree distribution plots
  * Power-law fitting plots
  * PageRank visualizations
* **Cypher Scripts** (Neo4j):

  * Export and load graph data to Neo4j.
  * Advanced querying of dependencies and high-degree nodes.

---

## Key Files Explained

| File/Folder       | Purpose                                     |
| ----------------- | ------------------------------------------- |
| `build_graph.py`  | Builds the dependency graph                 |
| `metrics.py`      | Computes network metrics                    |
| `plots.py`        | Creates visualizations                      |
| `powerlaw_fit.py` | Fits and visualizes power-law distributions |
| `cypher-scripts/` | Ready-to-run Neo4j Cypher scripts           |
| `data/csv/`       | Preloaded CSV data for analysis             |
| `fig/`            | Auto-generated visualizations               |
| `demo.ipynb`      | Interactive demonstration notebook          |

---
<!-- 
## 💡 Contribution Guidelines

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with a detailed description.

--- -->

## License

This project is licensed under the **MIT License**.

---
