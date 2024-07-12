
def bfs(graph, start):
    queue = [start]
    visited = set([start])

    while queue:
        vertex = queue.pop(0)
        print(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
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

