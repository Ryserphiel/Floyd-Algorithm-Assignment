import math


INF = math.inf

# Original weighted graph
# graph = [[0, 7, INF, 8],
#          [INF, 0, 5, INF],
#          [INF, INF, 0, 2],
#          [INF, INF, INF, 0]]

# Bi-directional equal-weighted graph
# graph = [[0, 7, INF, 8],
#          [INF, 0, 5, INF],
#          [INF, 5, 0, 2],
#          [8, INF, 2, 0]]

# # Bi-directional unequal-weighted(doubled) graph
graph = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
         [INF, 10, 0, 2],
         [16, INF, 4, 0]]

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
print("Bi-directional unequal-weighted(doubled) graph output:")
for x in result:
    print(x)
