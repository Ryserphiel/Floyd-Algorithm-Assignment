import math


INF = math.inf

# Positive weighted graph
# graph = [[0, 7, INF, 8],
#          [INF, 0, 5, INF],
#          [INF, INF, 0, 2],
#          [INF, INF, INF, 0]]

# Negative weighted graph
# graph = [[0, 7, INF, 8],
#          [INF, 0, -5, INF],
#          [INF, INF, 0, 2],
#          [INF, INF, INF, 0]]

# # Negative cycle graph
graph = [[0, -7, INF, 8],
         [INF, 0, -5, INF],
         [INF, INF, 0, 2],
         [INF, INF, INF, 0]]

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


# Output positive weighted graph before any calculation
# print("Positive weighted edges graph:")
# for x in graph:
#     print(x)

# Output positive weighted graph with correct solution
# result = recursive_floyd(graph)
# print("Positive weighted edges output(correct):")
# for x in result:
#     print(x)


# Output negative weighted graph before any calculation
# print("Negative weighted edges graph:")
# for x in graph:
#     print(x)

# Output negative weighted graph with correct solution
# result = recursive_floyd(graph)
# print("Negative weighted edges output(correct):")
# for x in result:
#     print(x)


# Output a graph with negative cycle before any calculation
# result = recursive_floyd(graph)
# print("Negative cycle graph:")
# for x in result:
#     print(x)

# Out for a negative cycle graph
result = recursive_floyd(graph)
print("Negative cycle output(incorrect):")
for x in result:
    print(x)
