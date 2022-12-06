from collections import Counter
from collections import OrderedDict
import matplotlib.pyplot as plt
import networkx as nx

EDGES_FILE = '3980.edges'

def find_paths():
    result = []
    edges = nx.read_edgelist(EDGES_FILE)
    nodes = list(edges.nodes)
    for i, n in enumerate(nodes):
        for m in nodes[i+1:]:
            try:
                path_len = nx.dijkstra_path_length(edges, n, m)
                if path_len > 0:
                    result.append(path_len)
            except:
                pass
    dictionary = dict(OrderedDict(sorted(Counter(result).items())))
    plt.bar(list(dictionary.keys()), dictionary.values(), color='g')
    plt.title("Distribution of lengths of shortest paths between Nodes in Graphs")
    plt.show()

if __name__ == '__main__':
    find_paths()

