import matplotlib.colors as mcolors

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
    2: [0, 4],
    3: [0],
    4: [2]
}

def greedyColoring(adj, V):
    result = [-1] * V
    available = [False] * V
    result[0] = 0
    color_names = list(mcolors.TABLEAU_COLORS.keys())
    
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
        print(f"Vertex {u} ---> Color {color_names[result[u]]}")

    unique_colors = len(set(result))
    return unique_colors

colors_g1 = greedyColoring(g1, 5)
print("Number of colors used in graph 1:", colors_g1)
print("\n\n\n\n")

colors_graph = greedyColoring(graph, 5)
print("nNumber of colors used in graph 2:", colors_graph)
