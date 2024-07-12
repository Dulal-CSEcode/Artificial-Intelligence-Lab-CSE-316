graph = {
    'A': ['B', 'C', 'D'],
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
    for depth_limit in range(max_depth + 1):
        print(f"Iterative Deepening Search with depth limit: {depth_limit}")
        if dfs_recursive(graph, start, depth_limit, 0, set()):
            return

def dfs_recursive(graph, node, depth_limit, current_depth, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        if current_depth == depth_limit:
            return False
        if node not in graph:
            return False
        for neighbor in sorted(graph[node], reverse=True):
            if dfs_recursive(graph, neighbor, depth_limit, current_depth + 1, visited):
                return True
    return False

print( "Iterative Deepening Search:")
dfs(graph, 'A', 3)  # You can set the maximum depth limit as per your requirement
