import graphs
from connected import check_connected, find_connected
from cyclic import check_cyclic
from distance import largest_dijkstra, shortest_dijkstra


def add_edge(graph):
    source = int(input("Input the source node "))
    destination = int(input("Input the destination node "))
    weight = int(input("Input the distance between the two nodes "))
    # we do the searching using dijkstra, so negative cost edges makes it so it won't work
    # so, if we have negative cost edges, we make them 0
    if weight < 0:
         graphs.add_edge(graph,source,destination)
    else:
         graphs.add_edge(graph,source,destination,weight)

# i didn't know how to read three variables at once from a file, so i stored the values in a list
# and deleted them as i iterate through it 
def read_file(graph, filename):
    # for number in my file, put it in a list
    values = [int(n) for n in filename.read().split()]

    while values:
         source = values.pop(0)
         destination = values.pop(0)
         weight = values.pop(0)
         graphs.add_edge(graph,source,destination,weight)

def create_graph():
    graph = graphs.graph

    #print automatically puts \n at the end of the sentence
    print ("1. Read the graph from the keyboard")
    print ("2. Read the first test case from a file (connected and acyclic)")
    print ("3. Read the second test case from a file (connected and cyclic)")
    print ("4. Read the third test case from a file (disconnected and acyclic)")
    print ("5. Read the fourth test case from a file (disconnected and cyclic)")
    print ("0. Exit the program")
    choice = input ("Your choice: ")

    if choice == '1':
        no_edge = int(input("\nHow many nodes do you want to input? "))
        for i in range(no_edge):
            add_edge(graph)
    elif choice == '2':
        try:
            fp = open("TestCase1.txt","r")
        except IOerror:
            print("The file did not open")

        read_file(graph,fp)

        fp.close()
    elif choice == '3':
        try:
            fp = open("TestCase2.txt","r")
        except IOerror:
            print("The file did not open")

        read_file(graph,fp)

        fp.close()
    elif choice == '4':
        try:
            fp = open("TestCase3.txt","r")
        except IOerror:
            print("The file did not open")

        read_file(graph,fp)

        fp.close()
    elif choice == '5':
        try:
            fp = open("TestCase4.txt","r")
        except IOerror:
            print("The file did not open")

        read_file(graph,fp)

        fp.close()
    else:
        return

    return graph

def choose(graph):
    while graph:
        print ("\n1. Add one more edge to the graph")
        print ("2. Print the graph")
        print ("3. Check if the graph is connected")
        print ("4. Check if the graph is cyclic")
        print ("5. Print all the connected components")
        print ("6. Determine the shortest path between two nodes")
        print ("7. Determine the longest path between two nodes")
        print ("0. Exit the program")
        choice = input("Your choice: ")
        print ("")

        if choice == '1':
            add_edge(graph)
        elif choice == '2':
            graphs.print_graph(graph)
        elif choice == '3':
            check_connected(graph)
        elif choice == '4':
            check_cyclic(graph)
        elif choice == '5':
            components = find_connected(graph)
            print (components)
        elif choice == '6':
            source = int(input("Input the source node ")) 
            destination = int(input("Input the destination node "))
            shortest_dijkstra(graph,source,destination)
        elif choice == '7':
            source = int(input("Input the source node "))
            destination = int(input("Input the destination node "))
            largest_dijkstra(graph,source,destination)
        else:
            return