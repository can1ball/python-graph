from graphs import graph, defaultdict
import random

def DFS_connected(graph, source, visited, component = None):
    # we mark the node as visited
    visited[source] = True
    # components of the connected subgraphs
    if(component != None):
        component.append(source)

    # for every child of my node
    for edge in graph[source]:
        # if we did not visit the node, recurse on it
        if visited[edge[0]] == False:
            DFS_connected(graph,edge[0],visited, component)

# returns true if the graph is connected, otherwise false
def is_connected(graph):
    # create an empty dictionary for every node in the graph and mark them as unvisited
    # if i were to use a list, it would give an out of range index error
    visited = defaultdict(bool)
    # marking every node as not visited
    for node in graph:
        visited[node] = False
    
    # we don't care from which node we start, if it's not connected it won't reach the whole graph
    vertex = random.choice(list(graph.keys()))

    DFS_connected(graph,vertex,visited)

    # if even one is not visited, it's not connected
    for index in visited:
        if visited[index] == False:
            return False

    return True

def find_connected(graph):
    # create an empty dictionary for every node in the graph
    visited = defaultdict(bool)
    # marking them as not visited
    for node in graph:
        visited[node] = False

    # an empty list of lists, every component is a list
    connected = []

    # number of connected components in the graph
    connected_components = 0

    for node in graph:
        # an empty list for the connected components so far
        component = []
        # if the node is not visited yet, recurse on it
        if visited[node] == False:
            DFS_connected(graph, node, visited,component)
            connected_components += 1
            # append the components found so far
            connected.append(component)

    print ("There are", connected_components, "connected components")
    # return the list of every component
    return connected

# a helper function
def check_connected(graph):
    if is_connected(graph) == True:
        print ("The graph is connected")
    else:
        print ("The graph is disconnected")