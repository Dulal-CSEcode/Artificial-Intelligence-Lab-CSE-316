graph = {
    '0': ['1', '2', '3'],
    '1': ['0'],
    '2': ['0', '3', '4'],
    '3': ['0','2'],
    '4': ['2']
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

   
print(bfs(graph, '0'))

