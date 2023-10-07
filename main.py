import json
import argparse
from graph import UndirectedGraph

def load_input(input_filename):
    with open(input_filename, 'r') as input_file:
        input_data = json.load(input_file)
    return input_data

def save_output(output_filename, connectivity_results):
    with open(output_filename, 'w') as output_file:
        json.dump(connectivity_results, output_file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Check connectivity of pairs of nodes in an undirected graph.")
    parser.add_argument("input_filename", help="Path to the input JSON file")
    parser.add_argument(
        "--method", choices=["dfs_recursive", "dfs_iterative", "union_find"],
        default="dfs_recursive", help="Method for checking connectivity (default: dfs_recursive)"
    )
    
    args = parser.parse_args()
    input_filename = args.input_filename
    output_filename = input_filename.replace(".json", "_output.json")

    input_data = load_input(input_filename)

    # Create an instance of the UndirectedGraph class
    threshold = input_data["threshold"]
    graph = UndirectedGraph(threshold)

    # Add nodes and build edges in the graph
    for point in input_data["points"]:
        node_id = point["id"]
        x = point["x"]
        y = point["y"]
        graph.add_node(node_id, x, y)

    for node1 in input_data["points"]:
        for node2 in input_data["points"]:
            if node1["id"] < node2["id"]:
                graph.add_edge(node1["id"], node2["id"])

    # Check connectivity for pairs based on the selected method
    pairs = input_data.get("pairs", [])
    connectivity_results = []
    
    if args.method == "dfs_recursive":
        connectivity_results = [graph.are_connected_recursive(pair[0], pair[1]) for pair in pairs]
    elif args.method == "dfs_iterative":
        connectivity_results = [graph.are_connected_iterative(pair[0], pair[1]) for pair in pairs]
    elif args.method == "union_find":
        connectivity_results = [graph.are_connected_component(pair[0], pair[1]) for pair in pairs]
    
    # Save connectivity results to output file in the same path as input
    save_output(output_filename, connectivity_results)

if __name__ == "__main__":
    main()
