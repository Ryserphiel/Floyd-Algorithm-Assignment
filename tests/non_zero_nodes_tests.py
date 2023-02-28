import math


INF = math.inf

# A series of tests to check whether non-zero nodes will affect the formula

# Original graph with each of the nodes set correctly to 0
# graph = [[0, 7, INF, 8],
#          [INF, 0, 5, INF],
#          [INF, INF, 0, 2],
#          [INF, INF, INF, 0]]

# # # First node value changed to a non-zero value
# graph = [[3, 7, INF, 8],
#          [INF, 0, 5, INF],
#          [INF, INF, 0, 2],
#          [INF, INF, INF, 0]]

# # # Second node value changed to a non-zero value
# graph = [[3, 7, INF, 8],
#          [INF, 4, 5, INF],
#          [INF, INF, 0, 2],
#          [INF, INF, INF, 0]]

# # # Third node value changed to a non-zero value
# graph = [[3, 7, INF, 8],
#          [INF, 4, 5, INF],
#          [INF, INF, 5, 2],
#          [INF, INF, INF, 0]]

# # # Fourth node value changed to a non-zero value
graph = [[3, 7, INF, 8],
         [INF, 4, 5, INF],
         [INF, INF, 5, 2],
         [INF, INF, INF, 6]]


MAX_LENGTH = len(graph[0])


def recursive_floyd(distance):

    def shortest_path(start_node, end_node, intermediate):

        if intermediate < 0:
            return distance[start_node][end_node]

        return min(shortest_path(start_node, end_node, intermediate - 1),
                   shortest_path(start_node, intermediate, intermediate - 1)
                   + shortest_path(intermediate, end_node, intermediate - 1))

    for intermediate in range(MAX_LENGTH):
        for start_node in range(MAX_LENGTH):
            for end_node in range(MAX_LENGTH):
                distance[start_node][end_node] = shortest_path(
                    start_node, end_node, intermediate)
    return distance


result = recursive_floyd(graph)
print("Non-zero fourth node output:")
for x in result:
    print(x)
