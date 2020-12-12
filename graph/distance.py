from graphs import graph, defaultdict
#import infinit
from sys import maxsize

def print_solution(graph,dist,path,source,destination):
    # if the node we were trying to reach has not been updated, there is no path
    if dist[destination] == maxsize or destination not in graph:
        print ("There is no path between", source,"and", destination)
        return

    print (source, "->", destination, "with the distance", dist[destination], "and the path", end="  ")

    # print the path
    print (source, end="->")
    print_path(path,destination)
    print ("\n")

# a helper function to print the shortest path
def print_path(path, node):
    #if node no longer has any parent, exit the recursion
    if path[node] == -1:
        return

    #recurse on path
    print_path(path,path[node])

    #print the node
    print (node, end="->")

# a function to detect lowest cost edge
def min_distance(graph,dist,sptSet):
    min = maxsize
    min_index = 0

    for node in graph:
        # search for the node not in shortest path tree
        if dist[node] < min and sptSet[node] == False:
            min = dist[node]
            min_index = node

    # return the lowest cost edge
    return min_index

def shortest_dijkstra(graph,source,destination):
    # a dictionary for distances of every node
    dist = defaultdict(int)
    # shortest path tree set
    sptSet = defaultdict(bool)
    # the shortest path to print
    path = defaultdict(int)

    for node in graph:
        # set all the nodes as not visited
        sptSet[node] = False
        # set the distances as infinit
        dist[node] = maxsize
        # there is no path, yet
        path[node] = -1
            
    # set the distance from the searched node to itself as 0
    dist[source] = 0

    #keep track of how many nodes we have left
    for count in list(graph.keys()):
        # pick the minimum node vertex from the set of nodes not yet visited 
        # u is always equal to src in first iteration 
        u = min_distance(graph,dist,sptSet)

        # put the minimum distance node in the shortest path tree
        sptSet[u] = True

        # update dist value of the adjacent vertices of the picked vertex only if the current  
        # distance is greater than new distance and the vertex in not in the shotest path tree 
        for edge in graph[u]:
            if edge[1] > 0 and sptSet[edge[0]] == False and dist[edge[0]] > dist[u] + edge[1]:
                # puth the node we just updated in the shortest path 
                path[edge[0]] = u
                dist[edge[0]] = dist[u] + edge[1]

    # print the solution
    print_solution(graph,dist,path,source,destination)

# this function is the same as the one above, but the costs of the edges are now negative
# the graph G becomes -G, every cost is inverted, then we find the minimum path
# we invert the minimum path back to positive, that's the longest path
# this function calculate longest simple path, NP-hard
def largest_dijkstra(graph,source,destination):
    dist = defaultdict(int)
    sptSet = defaultdict(bool)
    path = defaultdict(int)

    for node in graph:
        sptSet[node] = False
        dist[node] = maxsize
        path[node] = -1
            
    dist[source] = 0

    for count in list(graph.keys()):
        u = min_distance(graph,dist,sptSet)

        sptSet[u] = True

        for edge in graph[u]:
            if edge[1] > 0 and sptSet[edge[0]] == False and dist[edge[0]] > dist[u] - edge[1]:
                path[edge[0]] = u
                dist[edge[0]] = dist[u] - edge[1]

    #every distance is negative, we need to revert it to positive numbers
    for index in dist:
        dist[index] = abs(dist[index])

    print_solution(graph,dist,path,source,destination)