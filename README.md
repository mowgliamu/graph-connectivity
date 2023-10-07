# Undirected Graph Connectivity Checker

This Python project provides a utility for checking the connectivity of pairs of nodes in an undirected graph. The graph is defined using a set of vertices with (x, y) coordinates, and nodes are considered linked if their Cartesian distance is below a specified threshold. The project offers three methods for connectivity checking: Depth-First Search (DFS) Recursive, DFS Iterative, and the Component (Union-Find) Approach.

## Usage

### Connectivity Checking

To check the connectivity of pairs of nodes in the graph, you can use the main.py script. This script accepts a JSON input file containing the graph data and provides options to choose from one of the three connectivity checking methods: DFS Recursive, DFS Iterative, or the Component (Union-Find) Approach.

#### Example Usage for Connectivity Checking

```bash
python main.py input.json --method dfs_recursive
```

Replace `input.json` with the path to your JSON input file. You can choose one of the following methods:

- dfs_recursive (Default)
- dfs_iterative
- union_find
  
The ouput will be written to a JSON file, indicating whether the pairs are connected or not.

### Additional Feature: Execution Time Comparison

To compare the execution times of the three connectivity checking methods, you can use the `compare_execution_time.py` script. This script measures the execution time for each method and reports the results.

#### Example Usage for Execution Time Comparison

```bash
python compare_execution_time.py input.json
```

Replace `input.json` with the path to your JSON input file. The script will display the execution times for DFS Recursive, DFS Iterative, and the Component (Union-Find) Approach.

## Input JSON Format

The input JSON file should have the following format:

```json
{
  "threshold": 120.0,
  "points": [
    {
      "y": 34.95169607701711,
      "x": 68.86475009715542,
      "id": 0
    },
    // Add more points here
  ],
  "pairs": [
    [0, 1],
    [1, 2],
    // Add more pairs to check connectivity
  ]
}
```

- threshold: The maximum distance for nodes to be considered linked.
- points: A list of vertices with (x, y) coordinates and unique identifiers (id).
- pairs: A list of node pairs to check for connectivity.

## Project Strcuture

The project is organized as follows:

- `graph.py`: Defines the `UndirectedGraph` class for creating and managing the graph.
- `main.py`: The main script for checking connectivity based on user-selected method.
- `test_graph.py`: Contains unit tests to verify the functionality of the program.
- `compare_execution_time.py`: A script for comparing execution times of different connectivity checking methods.
- `README.md`: This file, providing instructions and information about the project.

## Unit Tests

You can run the unit tests using the following command:

```bash
python -m unittest test_parser_custom
```
