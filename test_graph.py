import unittest
import json
from graph import UndirectedGraph

class TestUndirectedGraph(unittest.TestCase):

    def setUp(self):
        # Load input data from JSON file
        with open("examples/small/in.json", "r") as input_file:
            input_data = json.load(input_file)
        
        self.input_data = input_data

        # Create a graph instance
        self.graph = UndirectedGraph(input_data["threshold"])

        # Add nodes to the graph
        for point in input_data["points"]:
            node_id = point["id"]
            x = point["x"]
            y = point["y"]
            self.graph.add_node(node_id, x, y)

        # Add edges to the graph
        for node1 in input_data["points"]:
            for node2 in input_data["points"]:
                if node1["id"] < node2["id"]:
                    self.graph.add_edge(node1["id"], node2["id"])

        # Define the expected output for connectivity
        self.expected_output = [
            True,  # 0-15 are connected
            True,  # 0-2 are connected
            True,  # 8-12 are connected
            True,  # 5-22 are connected
            True,  # 27-10 are connected
            True,  # 30-20 are connected
            False,  # 8-22 are not connected
            False,  # 17-28 are not connected
            False,  # 0-5 are not connected
        ]

    def test_connectivity_dfs_recursive(self):
        # Test connectivity using DFS Recursive
        for i, pair in enumerate(self.expected_output):
            node1, node2 = self.input_data["pairs"][i]
            self.assertEqual(self.graph.are_connected_recursive(node1, node2), pair)

    def test_connectivity_dfs_iterative(self):
        # Test connectivity using DFS Iterative
        for i, pair in enumerate(self.expected_output):
            node1, node2 = self.input_data["pairs"][i]
            self.assertEqual(self.graph.are_connected_iterative(node1, node2), pair)

    def test_connectivity_union_find(self):
        # Test connectivity using Union-Find (Component Approach)
        for i, pair in enumerate(self.expected_output):
            node1, node2 = self.input_data["pairs"][i]
            self.assertEqual(self.graph.are_connected_component(node1, node2), pair)

if __name__ == "__main__":
    unittest.main()
