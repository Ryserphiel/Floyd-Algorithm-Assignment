import math

# Test values for INF
#INF = math.inf
INF = 11

graph = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
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


# Test cases for different values assigned to INF(no path)

# Output sample graph before any calculation
# print("Inputed graph matrix:")
# for x in graph:
#     print(x)

# Output correct and expected solution
# result = recursive_floyd(graph)
# print("Correct output:")
# for x in result:
#     print(x)

# Output incorrect solution when INF is less than the highest returned value.
# In this example, that would be 12, so setting INF = 11 will result in
# an incorrect solution.
result = recursive_floyd(graph)
print("Incorrect output:")
for x in result:
    print(x)
