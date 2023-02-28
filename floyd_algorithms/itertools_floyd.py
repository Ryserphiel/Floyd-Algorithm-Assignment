import sys
import itertools

# Retrieve and set the maximum value that the architecture
# of the platform can hold.
INF = sys.maxsize

# An example graph
graph = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
         [INF, INF, 0, 2],
         [INF, INF, INF, 0]]

# Calculate the number of nodes in the graph given as input
MAX_LENGTH = len(graph[0])


def itertools_floyd(distance):
    """A simple implementation of Floyd Warshall's algorithm using itertools.
    This code is provided by the University of Liverpool"""

    for intermediate, start_node, end_node in\
            itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):

        # Assume that if start_node and end_node are the same
        # then the distance would be zero.
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        # Return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
                                             distance[start_node][intermediate]
                                             + distance[intermediate][end_node])
    return distance


# Call the floyd_itertools function and store the returned result
result = itertools_floyd(graph)

# Display the entire graph in an attractive manner
print("The shortest route is:")
for x in result:
    print(x)
