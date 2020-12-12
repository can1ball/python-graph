from graphs import graph, defaultdict

def DFS_cyclic(graph, source, visited, parent):
    # mark the node as visited
    visited[source] = True

    # for every child of my node
    for edge in graph[source]:
        # if the child is visited yet, recurse on it
        if visited[edge[0]] == False:
            if(DFS_cyclic(graph,edge[0],visited,source)):
                return True
        # if an adjacent vertex is visited and not parent of current vertex, then there is a cycle 
        elif parent != edge[0]:
            return True

    return False

# returns true if the graph has a cycle, otherwise false
def is_cyclic(graph):
    # create an empty dictionary for every node in the graph and mark them as unvisited
    visited = defaultdict(bool)
    for node in graph:
        visited[node] = False

    # check for cycle in different DFS trees
    for node in graph:
        # if the node is not yet visited, call the function 
        # if the function returns true, then there is a cycle
        if visited[node] == False:
            if DFS_cyclic(graph, node, visited, -1):
                return True

    return False

# a helper function
def check_cyclic(graph):
    if is_cyclic(graph) == True:
         print ("The graph is cyclic")
    else:
         print ("The graph is acyclic")