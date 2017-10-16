import networkx as nx

# NETWORKX
try:
    import networkx as nx
except ImportError:
    raise ImportError("Networkx required for graph()")
except RuntimeError:
    print("Networkx unable to open")
    raise

# MATPLOTLIB
try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("Matplotlib required for draw()")
except RuntimeError:
    print("Matplotlib unable to open")
    raise

# CSV
try:
    import csv
except ImportError:
    raise ImportError("CSV required for read()")
except RuntimeError:
    print("CSV unable to open")
    raise


# Directed graphs, that is, graphs with directed edges
G=nx.Graph()
G=nx.DiGraph()

G.add_edge(2,3,weight=0.9)
G.add_nodes_from([2,3])

print(G.adj)

# READER
with open('small.csv', 'rb') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in csv_reader:
        print ', '.join(row)


# WRITER
with open('eggs.csv', 'wb') as csvfile:
    gph_writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    gph_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    gph_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



