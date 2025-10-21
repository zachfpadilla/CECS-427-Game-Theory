import networkx as nx

def verify_digraph(G):
    attributes = ['a', 'b']
    if not isinstance(G, nx.DiGraph):
        print("Not a valid nx digraph.")
        return False
    edges = G.edges(data=True)
    if not all(all(attr in data for attr in attributes) for _, _, data in G.edges(data=True)):
        print("Not all edges have both a and b as an attribute");
    return True

     
