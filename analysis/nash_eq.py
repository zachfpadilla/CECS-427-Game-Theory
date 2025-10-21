import networkx as nx
from .utils import edge_cost, total_cost_path
def nash_equilibrium(G, n, initial, final):
    paths = list(nx.all_simple_paths(G, source=initial, target=final))
    path_costs = [(path, total_cost_path(G, n, path)) for path in paths]
    return min(path_costs, key=lambda x: x[1])
