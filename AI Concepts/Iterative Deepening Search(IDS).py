graph = {
    'A': ['B', 'C', 'D'],  # Define a graph as an adjacency list where each node maps to a list of its neighboring nodes.
    'B': ['A', 'E', 'F'],
    'C': ['A', 'G'],
    'D': ['A', 'H', 'J'],
    'E': ['B', 'K', 'L'],
    'F': ['B'],
    'G': ['C', 'M'],
    'H': ['D', 'N', 'O'],
    'J': ['D', 'P'],
    'K': ['E'],
    'L': ['E'],
    'M': ['G'],
    'N': ['H'],  
    'O': ['H'],  
    'P': ['J'] 
}

def dfs(graph, start, max_depth):
    # Define a function to perform Iterative Deepening Depth-First Search (IDDFS) on a graph.
    for depth_limit in range(max_depth + 1):  # Iterate through depth limits from 0 to max_depth.
        print(f"Iterative Deepening Search with depth limit: {depth_limit}")
        # Call the recursive DFS function with the current depth limit.
        if dfs_recursive(graph, start, depth_limit, set()):
            return

def dfs_recursive(graph, node, depth_limit, visited):
    # Define a recursive function to perform depth-first search on the graph.
    if node not in visited:  # Check if the current node has not been visited yet.
        print(node)  # Print the current node.
        visited.add(node)  # Mark the current node as visited.
        if depth_limit == 0:  # Check if reached the depth limit.
            return False  # Return False to indicate reaching the depth limit.
        if node not in graph:  # Check if the current node has no neighbors.
            return False  # Return False to indicate no further exploration.
        for neighbor in sorted(graph[node], reverse=True):  # Iterate through neighbors in reverse order.
            # Recursively call DFS on unvisited neighbors with decremented depth limit.
            if dfs_recursive(graph, neighbor, depth_limit - 1, visited):
                return True  # If the target node is found, return True.
    return False  # Return False if the target node is not found within the depth limit.

print("Iterative Deepening Search(IDS):")  # Print a message indicating the start of IDDFS.
dfs(graph, 'A', 2)  # Call IDDFS starting from node 'A' with a maximum depth of 3.
