import random
from collections import deque

class Node:
    def __init__(self, x, y, level):
        self.x = x  # x−coordinate of the node
        self.y = y  # y−coordinate of the node
        self.level = level  # level of the node in the BFS tree

class BFS:
    def __init__(self, N):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Possible movement directions
        self.found = False  # Flag to indicate whether the goal is found
        self.goal_level = 0  # Level of the goal node
        self.N = N  # Size of the grid
        self.source = None  # Source node
        self.goal = None  # Goal node

    def init(self):
        # Initialize the grid with random obstacles
        graph = [[random.choice([0, 1]) for x in range(self.N)] for x in range(self.N)]

        # Print the generated matrix
        print("Generated Matrix:")
        for row in graph:
            print(row)


        source_x, source_y = map(int, input("Enter starting point (x y): ").split())
        goal_x, goal_y = map(int, input("Enter goal point (x y): ").split())
        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, float('inf'))

        # Perform BFS
        self.st_bfs(graph)

        # Print result
        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal_level)
        else:
            print("Goal cannot be reached from the starting block")

    def st_bfs(self, graph):
        queue = deque()
        queue.append(self.source)

        # Breadth−first search
        while queue:
            u = queue.popleft()  # Dequeue the front node

            # Explore neighbors
            for dx, dy in self.directions:
                v_x, v_y = u.x + dx, u.y + dy

                # Check if the neighbor is within grid boundaries and is a valid move
                if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1:
                    v_level = u.level + 1  # Increment level
                    if v_x == self.goal.x and v_y == self.goal.y:  # Check if the neighbor is the goal
                        self.found = True
                        self.goal_level = v_level
                        self.goal.level = v_level
                        return
                    graph[v_x][v_y] = 0  # Mark the neighbor as visited
                    child = Node(v_x, v_y, v_level)
                    queue.append(child)  # Enqueue the neighbor

if __name__ == "__main__":
    N = int(input("Enter the grid size (N): "))
    bfs = BFS(N)
    bfs.init()
