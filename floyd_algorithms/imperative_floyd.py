import math

INF = math.inf

# An example graph
graph = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
         [INF, INF, 0, 2],
         [INF, INF, INF, 0]]

# Calculate the number of nodes in the graph given as input
MAX_LENGTH = len(graph[0])


def imperative_floyd(distance):
    """This function is an example of Floyd Warshall's algorithm
    implemented in an imperative manner.
    The code is taken from: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/ 
    """

    # Initialize the solution matrix in the same manner as the graph matrix input
    distance = list(map(lambda start_node: list(
        map(lambda end_node: end_node, start_node)), distance))

    # Update the graph after calculating the shortest route
    for intermidiate in range(MAX_LENGTH):
        for start_node in range(MAX_LENGTH):
            for end_node in range(MAX_LENGTH):
                distance[start_node][end_node] = min(
                    distance[start_node][end_node],
                    distance[start_node][intermidiate]
                    + distance[intermidiate][end_node])
    return distance


# Call the floyd_imperative function and store the returned result
result = imperative_floyd(graph)

# Display the entire graph in an attractive manner
print("The shortest route is:")
for x in result:
    print(x)
