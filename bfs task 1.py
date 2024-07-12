graph = {
    'S': ['A', 'C', 'L'],
    'A': ['R','S'],
    'C': ['R', 'S'],
    'L': ['R','S'],
    'R': ['A', 'C', 'L']
}
def bfs(graph, start):
    visited = [] # List to keep track of visited nodes
    queue = [start] # Initialize a queue

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)
    
    return visited

   
print(bfs(graph, 'S'))

