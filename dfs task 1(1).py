graph = {
    'S': ['A', 'C', 'L'],
    'A': ['R','S'],
    'C': ['R', 'S'],
    'L': ['R','S'],
    'R': ['A', 'C', 'L']
}
visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("The Depth-First Search Result : ")
dfs(visited, graph,'S')  # Corrected line: separated by semicolon
