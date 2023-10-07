import json
import cProfile
from graph import UndirectedGraph
import timeit
import argparse

def measure_execution_time(graph, pairs, method):
    """
    Measure the execution time of a connectivity checking method.

    Args:
        graph (UndirectedGraph): An instance of the UndirectedGraph class with the specified threshold.
        pairs (list): A list of node pairs to check connectivity for.
        method (str): The method to use for connectivity checking (dfs_recursive, dfs_iterative, or union_find).

    Returns:
        function: A wrapper function for measuring execution time.
    """
    def wrapper():
        for pair in pairs:
            node1, node2 = pair
            if method == "dfs_recursive":
                graph.are_connected_recursive(node1, node2)
            elif method == "dfs_iterative":
                graph.are_connected_iterative(node1, node2)
            elif method == "union_find":
                graph.are_connected_component(node1, node2)
    return wrapper

def main():
    """
    Main function to compare execution times of connectivity checking methods.
    """
    parser = argparse.ArgumentParser(description="Compare execution times of connectivity checking methods.")
    parser.add_argument("input_file", help="Path to the input JSON file")
    args = parser.parse_args()

    # Load the input data from the provided JSON file
    with open(args.input_file, 'r') as file:
        input_data = json.load(file)

    # Create a graph instance with the specified threshold
    threshold = input_data["threshold"]
    graph = UndirectedGraph(threshold)

    # Add nodes to the graph
    points = input_data["points"]
    for point in points:
        node_id = point["id"]
        x = point["x"]
        y = point["y"]
        graph.add_node(node_id, x, y)

    # Add edges to the graph
    for node1 in points:
        for node2 in points:
            if node1["id"] < node2["id"]:
                graph.add_edge(node1["id"], node2["id"])

    # Define the pairs to check connectivity
    pairs_to_check = input_data["pairs"]

    # Measure execution time for each method
    methods = ["dfs_recursive", "dfs_iterative", "union_find"]
    for method in methods:
        execution_time = timeit.timeit(measure_execution_time(graph, pairs_to_check, method), number=10)
        print(f"{method.capitalize()} Execution Time:", execution_time)

if __name__ == '__main__':
    cProfile.run('main()')
