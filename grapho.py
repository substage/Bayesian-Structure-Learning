# https://networkx.github.io/documentation/networkx-1.9/tutorial/tutorial.html

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

# SYSTEM
try:
    import sys
except ImportError:
    raise ImportError("SYS required for ARGUMENTS()")
except RuntimeError:
    print("SYS unable to open")
    raise

# CSV
try:
    import csv
except ImportError:
    raise ImportError("CSV required for read()")
except RuntimeError:
    print("CSV unable to open")
    raise

# PANDAS
try:
    import pandas as pd
except ImportError:
    raise ImportError("PANDAS required for read()")
except RuntimeError:
    print("PANDAS unable to open")
    raise


# GRAPHO components
import graphoscore as oscore
import graphoshow as oshow

# GRAPH: that is used to find best
# initialGraph = nx.DiGraph()

# COMPUTE: method called to perform the whole job
# TODO: output both png and gph files
def compute(infile, outfile):
    graph = read(infile)
    oshow.plotGraph(graph, outfile + ".png")
    oshow.toString(graph)
    write(outfile)
    pass

# READ: a dataframe from a CSV inputfile
def read(infile):
    inputDF = getInputDF(infile)
    testQuery = [('age', 1), ('sex', 1)]
    filteredDF = queryDataframe(inputDF, testQuery)
    print(filteredDF)
    graph = getNewGraph("first")
    graph = addGraphNodes(graph, inputDF)
    return graph
    # print(graph.node['fare'])
    # nx.connected_components(graph)
    # graph.adj

    #print(inputDF)

    # .values
    # df.head()
    pass

# Graph vs DiGraph
# name=graphName
def getNewGraph(graphName):
    graph = nx.Graph(name=graphName)
    return graph

# def query(dataframe):
#     #print(inputDF.loc[(inputDF['age']==1) & (inputDF['sex']==2)])
#     print(dataframe.loc[(dataframe['age']==1) & (dataframe['sex']==2)][['age', 'sex']])
#     pass

# FILTER: reduce the dataframe to the rows that match a query, with only the columns that match the query
# queryArray = [('age', 1), ('sex', 2)]
def queryDataframe(dataframe, queryArray):
    filteredDF = dataframe
    fieldNames = []
    for tuple in queryArray:
        field_name = tuple[0]
        field_value = tuple[1]
        filteredDF = filteredDF.loc[(filteredDF[field_name] == field_value)]
        fieldNames.append(field_name)
    return filteredDF[fieldNames]

# READ: get dataframe, inferring columns
def getInputDF(infile):
    inputDF = pd.read_csv(infile, header='infer')
    return inputDF

def addGraphNodes(graph, dataframe):
    for col in list(dataframe):
        # len()
        unique = dataframe[col].unique()
        print"{} \t\t UNIQUE: \t\t {} ".format(col, unique)
        graph.add_node(col)
        # graph.add_edge('age', col)
        #graph.add_nodes_from([2, 3])
        #print(dataframe.col)
    return graph


# WRITE: a gph output file
def write(outfile):
    with open(outfile, 'wb') as csvfile:
        gph_writer = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        gph_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
        gph_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    pass

def analizeGraph(graph):
    # degree()
    nx.connected_components
    # graph.adj



# FUTURE WORK
#