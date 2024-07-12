import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Define the first graph with vertices and their adjacent vertices
g1 = {
    0: [1, 2],
    1: [2, 3, 0],
    2: [3, 1, 0],
    3: [1, 2, 4],
    4: [3]
}

# Define the second graph with vertices and their adjacent vertices
graph = {
    0: [1, 2, 3],
    1: [0],
    2: [0, 4],
    3: [0],
    4: [2]
}

# Function to perform greedy graph coloring
def greedyColoring(adj, V):
    # Initialize a list to store the color of each vertex
    result = [-1] * V
    # Initialize a list to keep track of available colors for each vertex
    available = [False] * V
    # Assign the first vertex the color 0
    result[0] = 0
    # List of color names
    color_names = list(mcolors.TABLEAU_COLORS.keys())
    # Loop through each vertex starting from the second one
    for u in range(1, V):
        # Check each adjacent vertex of the current vertex
        for i in adj[u]:
            # Mark the color of adjacent vertices as unavailable
            if result[i] != -1:
                available[result[i]] = True
        # Find the first available color
        cr = 0
        while cr < V:
            if not available[cr]:
                break
            cr += 1
        # Assign the found color to the current vertex
        result[u] = cr
        # Reset the available colors for the next iteration
        for i in adj[u]:
            if result[i] != -1:
                available[result[i]] = False
    # Print the result, showing the color assigned to each vertex
    for u in range(V):
        print(f"Vertex {u} ---> Color {color_names[result[u]]}")

    # Count the unique colors used
    unique_colors = len(set(result))
    return unique_colors

# Perform greedy graph coloring for the first graph
colors_g1 = greedyColoring(g1, 5)
print("Number of colors used in graph 1:", colors_g1)

# Perform greedy graph coloring for the second graph
colors_graph = greedyColoring(graph, 5)
print("Number of colors used in graph 2:", colors_graph)
