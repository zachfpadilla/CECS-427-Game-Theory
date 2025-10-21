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

n = args.n
initial = args.initial
final = args.final

print(f"nash_equilibrium: {nash_equilibrium(G, n, initial, final)}")

if args.plot:
    visualize_graph(G)

