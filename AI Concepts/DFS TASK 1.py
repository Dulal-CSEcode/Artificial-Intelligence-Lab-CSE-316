graph = {
    'S': ['A', 'C', 'L'],
    'A': ['R', 'S'],
    'C': ['R', 'S'],
    'L': ['R', 'S'],
    'R': ['A', 'C', 'L']
}
def dfs(graph, start):
    visited = set()  
    #set track of visited nodes
    
    stack = [start]  
    #initialize the stack  starting node

    #the loop until stack empty
    while stack:
        node = stack.pop()  
        #pop a node from the stack
        
        if node not in visited: 
            #check if node not visited
            
            print(node) 
            visited.add(node)             
            #mark the node as visited
            
            #sort  adjacent nodes alphabetically in reverse order to maintain alphabetical order
            neighbors = sorted(graph[node], reverse=True)
            stack.extend(neighbors) 



print("Following is the Depth-First Search (using stack) :")

dfs(graph, 'S')
