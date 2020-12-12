from collections import defaultdict

# create an empty dictionary of lists, it range can vary
# the dictionary is like key : [list of values]
graph = defaultdict(list)

#create the graph, edge by edge
def add_edge(graph,source,destination,weight = 0):
    # we add at the key source the list made of destination node and weight
    graph[source].append([destination,weight])
    # because it's a unordered graph, we add the destionation key too
    graph[destination].append([source,weight])

def print_graph(graph):
    # for every key in my dictionary
    for node in graph:
        print (node, end = ": ")
        # for every list of the key
        for edge in graph[node]:
            # print the first element of the pair (node, weight)
            print (edge[0], end = " ")
        print ("")