# Using a Python dictionary to act as an adjacency list
graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D', 'S'],
    'B': ['E', 'S'],
    'C': ['F', 'S'],
    'D': ['A', 'G'],
    'E': ['B', 'G'],
    'F': ['C', 'G'],
    'G': ['D', 'E', 'F']
}

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            # Sort the adjacent nodes alphabetically
            neighbors = sorted(graph[node], reverse=True)  # To maintain alphabetical order
            stack.extend(neighbors)

print("Following is the Depth-First Search (using stack) :")
dfs(graph, 'S') 