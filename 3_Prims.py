import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices + 1  
        self.graph = [[0 for _ in range(self.V)] for _ in range(self.V)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        parent = [-1] * self.V
        key = [sys.maxsize] * self.V
        mst_set = [False] * self.V

        key[0] = 0  # Start from vertex 0
        parent[0] = -1

        total_weight = 0

        for _ in range(self.V - 1):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        print("Edge \tWeight")
        for i in range(1, self.V):  # Start from vertex 1 for printing MST
            if parent[i] != -1:
                print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
                total_weight += self.graph[i][parent[i]]
            else:
                print("-1 -", i, "\t", self.graph[i][parent[i]])

        print("Total Weight of Minimum Spanning Tree:", total_weight)


# Example usage:

V = int(input("Enter the number of vertices: "))
graph = Graph(V)

E = int(input("Enter the number of edges: "))

for _ in range(E):
    u, v, weight = map(int, input("Enter edge and its weight (u v weight): ").split())
    graph.add_edge(u, v, weight)

print("Minimum Spanning Tree:")
graph.prim_mst()
