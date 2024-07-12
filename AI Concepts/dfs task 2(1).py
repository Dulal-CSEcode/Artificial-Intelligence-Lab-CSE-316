graph = {
    '0': ['1', '2', '3'],
    '1': ['0'],
    '2': ['0', '3', '4'],
    '3': ['0','2'],
    '4': ['2']
}
visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("The Depth-First Search Result : ")
dfs(visited, graph, '0')  # Corrected line: separated by semicolon
