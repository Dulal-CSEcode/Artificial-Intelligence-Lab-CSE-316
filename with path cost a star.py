from collections import deque

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        H = {
            'S': 5,
            'A': 3,
            'B': 3,
            'C': 2,
            'D': 6,
            'E': 3,
            'G': 0
        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node

        while open_list:
            n = min(open_list, key=lambda x: g[x] + self.h(x))

            if n == stop_node:
                reconst_path = []
                cost = g[n]
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Path found:', reconst_path)
                print('Cost of the path:', cost)
                return reconst_path, cost

            open_list.remove(n)
            closed_list.add(n)

            for (m, weight) in self.get_neighbors(n):
                if m in closed_list:
                    continue

                if m not in open_list:
                    open_list.add(m)
                    g[m] = g[n] + weight
                    parents[m] = n

                elif g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

        print('Path does not exist!')
        return None, None

adjacency_list = {
    'S': [('B', 2), ('A', 6), ('G', 10)],
    'A': [('B', 3), ('C', 1), ('S', 6)],
    'B': [('D', 6), ('A', 3), ('S', 2), ('E', 2)],
    'C': [('D', 4),('A', 1)],
    'D': [('B', 6), ('C', 4), ('E', 3)],
    'E': [('B', 2), ('D', 3), ('G', 1)],
    'G': []
}

graph1 = Graph(adjacency_list)

path, cost = graph1.a_star_algorithm('S', 'G')
