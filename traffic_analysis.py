import networkx as nx
from cli import get_parser
from analysis import *
from verification import verify_digraph
from visualization import visualize_graph
parser = get_parser()
args = parser.parse_args()

G = None

try:
    G = nx.read_gml(args.graph_file)
    print(f"Successfully loaded graph from '{args.graph_file}'.")
    print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
except FileNotFoundError:
    print(f"Error: The file '{args.graph_file}' was not found.")
    exit(1)
except Exception as e:
    print(f"Error: Failed to parse GML file. Reason: {e}")
    exit(1)

if not verify_digraph(G):
    exit(1)

n = 0
try:
    n = int(args.n)
    if n <= 0:
        print("Error: Number of vehicles 'n' must be a positive integer.")
        exit(1)
except ValueError:
    print("Error: 'n' must be an integer.")
    exit(1)

initial = args.initial
final = args.final

if not G.has_node(initial):
    print(f"Error: Initial node '{initial}' not in graph.")
    exit(1)
if not G.has_node(final):
    print(f"Error: Final node '{final}' not in graph.")
    exit(1)

flow_eq = nash_equilibrium(G, n, initial, final)
flow_so = social_optimum(G, n, initial, final)

print(f"Nash Equilibrium: {flow_eq}")
print(f"Social Optimum: {flow_so}")

print("\n--- Nash Equilibrium (User Optimum) ---")
if not flow_eq:
    print("No flow found.")
else:
    for (u, v), flow in flow_eq.items():
        if flow > 1e-6:
            print(f"Edge ({u} -> {v}): {flow:.4f} vehicles")

print("\n--- Social Optimum ---")
if not flow_so:
    print("No flow found.")
else:
    for (u, v), flow in flow_so.items():
        if flow > 1e-6:
            print(f"Edge ({u} -> {v}): {flow:.4f} vehicles")

if args.plot:
    print("\nGenerating plot...")
    visualize_graph(G, n, flow_eq, flow_so)

