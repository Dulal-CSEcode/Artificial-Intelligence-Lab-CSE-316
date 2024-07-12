graph = {
    '0': ['1', '2', '3'],
    '1': ['0'],
    '2': ['0', '3', '4'],
    '3': ['0','2'],
    '4': ['2']
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
dfs(graph, '0')