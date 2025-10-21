import argparse

#def validFileName(str):
#    """Returns the filename only if it follows valid naming scheme."""
#    file_name_array = str.split('.')
#    if len(file_name_array) != 2:
#        raise argparse.ArgumentTypeError('File name requires exactly one .gml extension.')
#    if file_name_array[1] != "gml":
#        raise argparse.ArgumentTypeError('File name must end in .gml.')
#    if re.search(r'[^A-Za-z\d_-]', file_name_array[0]):
#        raise argparse.ArgumentTypeError('File name must not contain non-alphanumeric characters.')
#    return str

def get_parser():
    """ Returns a custom argparse parser made for graph.py """
    parser = argparse.ArgumentParser(description='Python application that handles Girvan-Newman graph partitioning, edge removal, homophily/balance verification, and visualization.', formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("graph_file", help="Path to the input graph file in .gml format.")

    parser.add_argument("n", help="Number of vehicles in the network.")

    parser.add_argument("initial", help="Initial node in the graph.")

    parser.add_argument("final", help="Final node in the graph.")

    parser.add_argument("--plot", action="store_true", help="Creates a visualization of the traffic in the network.")

    return parser
