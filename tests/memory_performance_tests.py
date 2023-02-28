import math
import itertools
import tracemalloc

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


def memory_performance_checker():
    """This function test the current and peak memory usage of each Floyd's function"""

    # Track and display imperative_floyd function memory usage
    tracemalloc.start()
    imperative_floyd(graph)
    current_imper_memory, peak_imper_memory = tracemalloc.get_traced_memory()
    print("Memory utilisation for the imperative version of Floyd's algorithm:")
    print(f"Current memory usage: {current_imper_memory}")
    print(f"Peak memory usage: {peak_imper_memory}")
    tracemalloc.stop()

    # Track and display recursive_floyd function memory usage
    tracemalloc.start()
    recursive_floyd(graph)
    current_recur_memory, peak_recur_memory = tracemalloc.get_traced_memory()
    print("\nMemory utilisation for the recursive version of Floyd's algorithm:")
    print(f"Current memory usage: {current_recur_memory}")
    print(f"Peak memory usage: {peak_recur_memory}")
    tracemalloc.stop()

    # Track and display itertools_floyd function memory usage
    tracemalloc.start()
    itertools_floyd(graph)
    current_iter_memory, peak_iter_memory = tracemalloc.get_traced_memory()
    print("\nMemory utilisation for the itertool version of Floyd's algorithm:")
    print(f"Current memory usage: {current_iter_memory}")
    print(f"Peak memory usage: {peak_iter_memory}")
    tracemalloc.stop()


memory_performance_checker()
