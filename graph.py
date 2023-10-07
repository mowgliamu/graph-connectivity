import math
import json
from typing import Dict, Set, Tuple, Union, List

# Define type aliases for better clarity
Point = Tuple[float, float]
NodeID = int
NeighborSet = Set[NodeID]

class UndirectedGraph:
    def __init__(self, threshold: float):
        """
        Initialize an UndirectedGraph instance with a given distance threshold.

        Args:
            threshold (float): The maximum distance for nodes to be considered connected.
        """
        self.threshold = threshold
        self.graph: Dict[NodeID, Dict[str, Union[Point, NeighborSet]]] = {}

    def add_node(self, node_id: NodeID, x: float, y: float) -> None:
        """
        Add a node to the graph.

        Args:
            node_id (NodeID): The unique identifier for the node.
            x (float): The x-coordinate of the node.
            y (float): The y-coordinate of the node.
        """
        self.graph[node_id] = {"coords": (x, y), "neighbors": set()}

    def add_edge(self, node1: NodeID, node2: NodeID) -> None:
        """
        Add an edge between two nodes if they are within the specified distance.

        Args:
            node1 (NodeID): The identifier of the first node.
            node2 (NodeID): The identifier of the second node.
        """
        x1, y1 = self.graph[node1]["coords"]
        x2, y2 = self.graph[node2]["coords"]
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if distance < self.threshold:
            self.graph[node1]["neighbors"].add(node2)
            self.graph[node2]["neighbors"].add(node1)

    def get_edges(self) -> List[Tuple[NodeID, NodeID]]:
        """
        Get a list of edges in the graph.

        Returns:
            List[Tuple[NodeID, NodeID]]: A list of edge tuples, where each tuple represents
            a pair of connected nodes.
        """
        edges = []
        for node1, neighbors in self.graph.items():
            for node2 in neighbors["neighbors"]:
                if node1 < node2:  # Avoid duplicate edges
                    edges.append((node1, node2))
        return edges

    def get_adjacency_list(self) -> Dict[NodeID, List[NodeID]]:
        """
        Get the adjacency list representation of the graph.

        Returns:
            Dict[NodeID, List[NodeID]]: A dictionary where keys are node identifiers, and
            values are lists of connected neighbor nodes.
        """
        adjacency_list = {}
        for node, neighbors in self.graph.items():
            adjacency_list[node] = list(neighbors["neighbors"])
        return adjacency_list

    def are_connected_recursive(self, node1: NodeID, node2: NodeID) -> bool:
        """
        Check if two nodes are connected using a recursive Depth-First Search (DFS) approach.

        Args:
            node1 (NodeID): The identifier of the first node.
            node2 (NodeID): The identifier of the second node.

        Returns:
            bool: True if the nodes are connected, False otherwise.
        """
        visited = set()

        def dfs(current_node):
            if current_node == node2:
                return True
            visited.add(current_node)
            for neighbor in self.graph[current_node]["neighbors"]:
                if neighbor not in visited and dfs(neighbor):
                    return True
            return False

        return dfs(node1)

    def are_connected_iterative(self, node1: NodeID, node2: NodeID) -> bool:
        """
        Check if two nodes are connected using an iterative Depth-First Search (DFS) approach.

        Args:
            node1 (NodeID): The identifier of the first node.
            node2 (NodeID): The identifier of the second node.

        Returns:
            bool: True if the nodes are connected, False otherwise.
        """
        visited = set()
        stack = [node1]

        while stack:
            current_node = stack.pop()
            visited.add(current_node)

            if current_node == node2:
                return True

            for neighbor in self.graph[current_node]["neighbors"]:
                if neighbor not in visited and neighbor not in stack:
                    stack.append(neighbor)

        return False

    def find_parent(self, parent: List[NodeID], node: NodeID) -> NodeID:
        """
        Find the parent node of a given node in the Union-Find data structure.

        Args:
            parent (List[NodeID]): The parent array representing the component structure.
            node (NodeID): The identifier of the node to find the parent for.

        Returns:
            NodeID: The identifier of the parent node.
        """
        if parent[node] == -1:
            return node
        #if parent[node] != node:
        parent[node] = self.find_parent(parent, parent[node])
        return parent[node]

    def union(self, parent: List[NodeID], x: NodeID, y: NodeID) -> None:
        """
        Perform a union operation to merge two components in the Union-Find data structure.

        Args:
            parent (List[NodeID]): The parent array representing the component structure.
            x (NodeID): The identifier of the first node/component.
            y (NodeID): The identifier of the second node/component.
        """
        root_x = self.find_parent(parent, x)
        root_y = self.find_parent(parent, y)
        parent[root_x] = root_y
        
    def are_connected_component(self, node1: NodeID, node2: NodeID) -> bool:
        """
        Check if two nodes are connected using the Component (Union-Find) Approach.

        Args:
            node1 (NodeID): The identifier of the first node.
            node2 (NodeID): The identifier of the second node.

        Returns:
            bool: True if the nodes are connected, False otherwise.
        """
        n = len(self.graph)
        parent = [-1] * n

        for node in range(n):
            for neighbor in self.graph[node]["neighbors"]:
                if self.find_parent(parent, node) != self.find_parent(parent, neighbor):
                    self.union(parent, node, neighbor)

        return self.find_parent(parent, node1) == self.find_parent(parent, node2)