import networkx as nx
import matplotlib.pyplot as plt
from analysis import *

def visualize_graph(G, plot_type):
    """Visualizes the graph based on computed metrics."""
    if G.number_of_nodes() == 0:
        print("Cannot plot an empty graph.")
        return

    print(f"Generating plot for type: '{plot_type}'...")
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G, seed=42)

    if plot_type == 'C':  # Clustering Coefficient
        compute_clustering_coefficients(G)
        node_sizes = [d.get('clustering_coefficient', 0) * 2000 + 100 for n, d in G.nodes(data=True)]
        node_colors = [G.degree(n) for n in G.nodes()]
        nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.viridis,
                font_color='white')
        plt.title("Graph Visualization: Clustering Coefficient & Degree")

    elif plot_type == 'N':  # Neighborhood Overlap
        compute_neighborhood_overlap(G)
        edge_widths = [d.get('neighborhood_overlap', 0) * 5 + 0.5 for u, v, d in G.edges(data=True)]
        # Edge color based on sum of degrees of endpoints
        edge_colors = [G.degree(u) + G.degree(v) for u, v in G.edges()]
        nx.draw(G, pos, with_labels=True, width=edge_widths, edge_color=edge_colors, edge_cmap=plt.cm.plasma)
        plt.title("Graph Visualization: Neighborhood Overlap & Degree Sum")

    elif plot_type == 'P':  # Properties (color/sign)
        node_colors = [d.get('color', 'skyblue') for n, d in G.nodes(data=True)]

        pos_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get('sign', 1) >= 0]
        neg_edges = [(u, v)  for u, v, d in G.edges(data=True) if d.get('sign', 1) < 0]

        nx.draw_networkx_nodes(G, pos, node_color=node_colors)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edgelist=pos_edges, edge_color='g', width=1.5)
        nx.draw_networkx_edges(G, pos, edgelist=neg_edges, edge_color='r', style='dashed', width=1.5)
        plt.title("Graph Visualization: Node/Edge Properties (color/sign)")
    elif plot_type =='T': # unused T type, possibly temporal simulation. Flag already exists. Continue without error.
        return
    else:
        print(f"Unknown plot type: {plot_type}. Defaulting to basic plot.")
        nx.draw(G, pos, with_labels=True, node_color='skyblue')

    plt.show()
