import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def visualize_graph(G, n_vehicles, flow_eq, flow_so):
    """Visualizes the graph based on computed metrics."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
    fig.suptitle(f"Traffic Analysis for {n_vehicles} Vehicles", fontsize=16)

    pos = nx.kamada_kawai_layout(G)
    nx.draw_networkx_nodes(G, pos, ax=ax1, node_color='#add8e6', node_size=700)
    nx.draw_networkx_labels(G, pos, ax=ax1, font_weight='bold')
    nx.draw_networkx_edges(G, pos, ax=ax1, node_size=700,
                           arrowstyle='->', arrowsize=20,
                           connectionstyle='arc3,rad=0.1')

    edge_labels = {}
    for u, v, data in G.edges(data=True):
        a = data['a']
        b = data['b']
        eq_flow = flow_eq.get((u, v), 0.0)
        so_flow = flow_so.get((u, v), 0.0)
        label = (
            f"C(x) = {a:.1f}x + {b:.1f}\n"
            f"Eq. Flow: {eq_flow:.2f}\n"
            f"SO. Flow: {so_flow:.2f}"
        )
        edge_labels[(u, v)] = label

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax1,
                                 font_size=9, bbox=dict(alpha=0.1, boxstyle='round,pad=0.2'))
    ax1.set_title("Network Graph and Flow Distribution")
    ax1.axis('off')

    #set x-axis range slightly larger than N to show behavior
    x_range = np.linspace(0, n_vehicles * 1.2, 100)

    for u, v, data in G.edges(data=True):
        a = data['a']
        b = data['b']

        #c(x) = ax + b
        cost = a * x_range + b
        #mc(x) = 2ax + b
        marginal_cost = 2 * a * x_range + b

        label_str = f"({u}→{v})"

        line, = ax2.plot(x_range, cost, label=f"C(x) {label_str}")
        ax2.plot(x_range, marginal_cost, linestyle='--', color=line.get_color(),
                 label=f"MC(x) {label_str}")

    ax2.set_title("Edge Cost Functions")
    ax2.set_xlabel("Number of Vehicles (x)")
    ax2.set_ylabel("Travel Cost (Time)")
    ax2.axvline(x=n_vehicles, color='r', linestyle=':', label=f"Total Vehicles (N={n_vehicles})")
    ax2.legend(fontsize='small', ncol=2)
    ax2.grid(True, linestyle=':', alpha=0.7)
    ax2.set_ylim(bottom=0)
    ax2.set_xlim(left=0)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    print("\nDisplaying plot... Close the plot window to exit.")
    plt.show()
