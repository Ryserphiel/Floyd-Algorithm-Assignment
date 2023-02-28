import math

INF = math.inf

# An example graph
graph = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
         [INF, INF, 0, 2],
         [INF, INF, INF, 0]]

# Calculate the number of nodes in the graph given as input
MAX_LENGTH = len(graph[0])


def recursive_floyd(distance):
    """This function is an example of Floyd Warshall's Algoritm 
    implemented using recursion.
    """

    # This is the recursive formula for determining
    # the shortest path between two nodes.

    def shortest_path(start_node, end_node, intermediate):

        # After attempting all intermediate nodes and calculating
        # the direct pathways, exits the recursion.
        # This is the case when intermediate < 0 since index 0 represents the root node
        if intermediate < 0:
            return distance[start_node][end_node]

        # If travelling via intermediate nodes is shorter
        # then return it as the shorter distance.
        return min(shortest_path(start_node, end_node, intermediate - 1),
                   shortest_path(start_node, intermediate, intermediate - 1)
                   + shortest_path(intermediate, end_node, intermediate - 1))

    # Update the graph after calculating the shortest route
    for intermediate in range(MAX_LENGTH):
        for start_node in range(MAX_LENGTH):
            for end_node in range(MAX_LENGTH):
                distance[start_node][end_node] = shortest_path(
                    start_node, end_node, intermediate)
    return distance


# Call the floyd_recursive function and store the returned result
result = recursive_floyd(graph)

# Display the entire graph in an attractive manner
print("The shortest route is:")
for x in result:
    print(x)
