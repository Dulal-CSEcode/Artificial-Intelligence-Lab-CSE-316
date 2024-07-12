g1 = {
    0: [1, 2],
    1: [2, 3, 0],
    2: [3, 1, 0],
    3: [1, 2, 4],
    4: [3]
}

graph = {
    0: [1, 2, 3],
    1: [0],
    2: [0, 3, 4],
    3: [0, 2],
    4: [2]
}

def greedyColoring(adj, V):
    result = [-1] * V
    available = [False] * V
    result[0] = 0
    for u in range(1, V):
        for i in adj[u]:
            if result[i] != -1:
                available[result[i]] = True
        cr = 0
        while cr < V:
            if not available[cr]:
                break
            cr += 1
        result[u] = cr
        for i in adj[u]:
            if result[i] != -1:
                available[result[i]] = False
    for u in range(V):
        print("Vertex", u, " --->  Color", result[u])

print("coloring of graph 1")
greedyColoring(g1, 5)

print("coloring of graph 2")
greedyColoring(graph, 5)
