class Queue:
    """
    A simple implementation of a FIFO queue.
    """

    def __init__(self):
        """
        Initialize the queue.
        """
        self.__queue = []

    def __len__(self):
        """
        Returns: an integer representing the number of items in the queue.
        """
        length = len(self.__queue)
        return length

    def __str__(self):
        """
        Returns: a string representation of the queue.
        """
        string_rep = ""
        for element in self.__queue:
            string_rep += str(element)
        return string_rep

    def push(self, item):
        """
        Add item to the queue.

        input:
            - item: any data type that's valid in a list
        """
        #Appends at the end, following FIFO principles
        self.__queue.append(item)

    def pop(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the queue.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        #The element at the beginning of the list 
        #is the one that was first appended, 
        #and thus must be the first to leave
        first = self.__queue.pop(0)
        return first

    def clear(self):
        """
        Remove all items from the queue.
        """
        self.__queue = []

class Stack:
    """
    A simple implementation of a LIFO stack.
    """
    def __init__(self):
        """
        Initialize the stack.
        """
        self.__stack = []

    def __len__(self):
        """
        Returns: an integer representing the number of items in the stack.
        """
        length = len(self.__stack)
        return length

    def __str__(self):
        """
        Returns: a string representation of the stack.
        """
        string_rep = ""
        for element in self.__stack:
            string_rep += str(element)
        return string_rep

    def push(self, item):
        """
        Add item to the stack.

        input:
            - item: any data type that's valid in a list
        """
        #Inserts at the beginning, following LIFO principles
        self.__stack.insert(0, item)

    def pop(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the queue.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        #The element at the beginning of the list 
        #is the one that was last appended, 
        #and thus must be the first to leave
        top = self.__stack.pop(0)
        return top

    def clear(self):
        """
        Remove all items from the queue.
        """
        self.__stack = []


def bfs_dfs(graph, rac_class, start_node, end_node):
    """
    Performs a breadth-first search or a depth-first search on graph
    starting at the start_node.  The rac_class should either be a
    Queue class or a Stack class to select BFS or DFS.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - rac_class: a restricted access container (Queue or Stack) class to
          use for the search
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end

    Returns: a dictionary associating each visited node with its parent
    node.
    """
    #Initializing empty queue or stack
    container = rac_class()
    #Will hold the distance of each node from the starting node
    dist = {}
    #Will hold the parent of each node
    parent = {}
    #Sets the default distance to infinity and the default parent to None
    for node in graph.nodes():
        dist[node] = float("inf")
        parent[node] = None
    #Distance between the start node and itself is 0
    dist[start_node] = 0
    #Push the starting node into the container
    container.push(start_node)
    #Iterate through the container while nodes still need to be traversed
    while len(container) > 0:
        print(str(container))
        #Take out the first in node to check
        node = container.pop()
        #If we've reached the end node, we can stop
        if node == end_node:
            break
        #Similarly, after finding the end node, any nodes
        #of equal distance from the start no longer need to
        #be checked
        if dist[node] == dist[end_node]:
            break
        #Store the relevant data about node's neighbors
        for nbr in graph.get_neighbors(node):
            if dist[nbr] == float("inf"):
                if dist[node] + 1 == dist[end_node]:
                    break
                dist[nbr] = dist[node] + 1
                parent[nbr] = node
                container.push(nbr)

 
    return parent


def dfs(graph, start_node, end_node, parent):
    """
    Performs a recursive depth-first search on graph starting at the
    start_node.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end
        - parent: a dictionary that initially has one entry associating
                  the original start_node with None

    Modifies the input parent dictionary to associate each visited node
    with its parent node
    """
    #print(parent)  
    #Access neighbors of start node
    neighbors = graph.get_neighbors(start_node)
    #Check if all of them are in parents
    new_nbrs = False
    for check_node in neighbors:
        if check_node not in parent:
            new_nbrs = True
            break
    #Base Case: start_node has no new neighbors
    if new_nbrs == False:
        return None
    #Recursive Case: start_node has a non-zero number of new neigbhors
    else:
        #Only traverse neighbors that have not already been traversed
        non_visited_nbrs = [node for node in neighbors if node not in parent]
        for nbr in non_visited_nbrs:
            #If end node has been added, do not check any more neighbors
            if end_node in parent:
                break
            parent[nbr] = start_node
            dfs(graph, nbr, end_node, parent)
    if end_node in parent:
        return parent
    return None

#Testing
#print(maps.load_test_graph('asymmetric1'))
#print(dfs(maps.load_test_graph('asymmetric1'), 'C', 'H', {'C': None}))

def astar(graph, start_node, end_node,
          edge_distance, straight_line_distance):
    """
    Performs an A* search on graph starting at start_node.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end
        - edge_distance: a function which takes two nodes and a graph
                         and returns the actual distance between two
                         neighboring nodes
        - straight_line_distance: a function which takes two nodes and
                         a graph and returns the straight line distance 
                         between two nodes

    Returns: a dictionary associating each visited node with its parent
    node.
    """
    #print(graph)
    
    parent = {}
    
    #Initialize dictionaries to store g and h costs for 
    #each node. The f cost can be calculated by simply
    #adding the g and h costs for a given node.
    g_costs = {}
    h_costs = {}
    
    
    #Initalize the openset and closedset
    open_set = []
    closed_set = []
    
    #Initialize values for the start node
    g_costs[start_node] = 0
    h_costs[start_node] = straight_line_distance(start_node, end_node, graph)
    parent[start_node] = None
    
    #Add the start_node to the open_set
    open_set.append(start_node)
    
    #Keep searching until the openset is empty or until end_node is found
    while len(open_set) > 0:
        #print("Openset", open_set)
        #Find the node in openset with the lowest f cost
        min_f = float("inf")
        min_node = ""
        for node_checker in open_set:
            #If a lower f cost is found in the openset, update
            #If they are equal, use the first node added to the openset
            if g_costs[node_checker] + h_costs[node_checker] < min_f:
                min_f = g_costs[node_checker] + h_costs[node_checker]
                min_node = node_checker
                
        #Move min_node to the closed set
        open_set.remove(min_node)
        closed_set.append(min_node)
        
        if min_node == end_node:
            break
        

        for nbr in graph.get_neighbors(min_node):
            #print(parent)
            #print("Neighbor", nbr)
            #Case 1: nbr is in closed set --> Do nothing
            if nbr in closed_set:
                pass
            #Case 2: nbr is in open set --> Check if g can be lowered
            #If so, update parent dictionary because shorter route found
            elif nbr in open_set:
                nbr_g = g_costs[min_node] + edge_distance(min_node, nbr, graph)
                if nbr_g < g_costs[nbr]:
                    g_costs[nbr] = nbr_g
                    parent[nbr] = min_node
            #Case 3: nbr is in neither sets --> Calculate g and h, 
            #add to parent
            else:
                nbr_g = g_costs[min_node] + edge_distance(min_node, nbr, graph)
                g_costs[nbr] = nbr_g
                h_costs[nbr] = straight_line_distance(nbr, end_node, graph)
                parent[nbr] = min_node
                open_set.append(nbr)
    
    return parent
