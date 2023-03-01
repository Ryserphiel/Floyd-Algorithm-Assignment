import math
import itertools
import time

INF = math.inf

graph = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
         [INF, INF, 0, 2],
         [INF, INF, INF, 0]]

MAX_LENGTH = len(graph[0])


def imperative_floyd(distance):

    distance = list(map(lambda start_node: list(
        map(lambda end_node: end_node, start_node)), distance))

    for intermidiate in range(MAX_LENGTH):
        for start_node in range(MAX_LENGTH):
            for end_node in range(MAX_LENGTH):
                distance[start_node][end_node] = min(
                    distance[start_node][end_node],
                    distance[start_node][intermidiate]
                    + distance[intermidiate][end_node])
    return distance


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


def itertools_floyd(distance):

    for intermediate, start_node, end_node in\
            itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):

        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        distance[start_node][end_node] = min(distance[start_node][end_node],
                                             distance[start_node][intermediate]
                                             + distance[intermediate][end_node])
    return distance


def speed_performance_checker():
    """This function test the average execution time of each Floyd's function
    for 10,000 cycles.
    """

    cycle = 10000
    start_time = time.time()
    for _ in range(cycle):
        imperative_floyd(graph)
    end_time = time.time()
    imperative_speed = end_time - start_time

    start_time = time.time()
    for _ in range(cycle):
        recursive_floyd(graph)
    end_time = time.time()
    recursive_speed = end_time - start_time

    start_time = time.time()
    for _ in range(cycle):
        itertools_floyd(graph)
    end_time = time.time()
    itertools_speed = end_time - start_time

    return (imperative_speed, recursive_speed, itertools_speed)


# Store the result of the performance speed tests
round_imperative_speed, round_recursive_speed, round_itertools_speed = speed_performance_checker()

# Round the speed performance results to two decimal places
round_imperative_speed = round(round_imperative_speed, 2)
round_recursive_speed = round(round_recursive_speed, 2)
round_itertools_speed = round(round_itertools_speed, 2)

# Print out the results
print(f"Imperative speed performance: {round_imperative_speed}s")
print(f"Recursive speed performance: {round_recursive_speed}s")
print(f"Itertool speed performance: {round_itertools_speed}s")
