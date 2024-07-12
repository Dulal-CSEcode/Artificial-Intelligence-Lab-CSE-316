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
    2: [0, 3, 4],
    3: [0, 2],
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
        print("Vertex", u, " --->  Color", result[u])

# Perform greedy graph coloring for the first graph
print("coloring of graph 1")
greedyColoring(g1, 5)

# Perform greedy graph coloring for the second graph
print("coloring of graph 2")
greedyColoring(graph, 5)
