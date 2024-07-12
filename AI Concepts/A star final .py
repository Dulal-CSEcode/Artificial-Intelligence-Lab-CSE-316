from collections import deque

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
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

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)
                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):

                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

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

graph1.a_star_algorithm('S', 'G')
