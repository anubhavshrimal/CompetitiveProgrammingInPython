from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, frm, to, weight):
        self.graph[frm].append([to, weight])

        if self.directed is False:
            self.graph[to].append([frm, weight])
        else:
            self.graph[to] = self.graph[to]

    def find_min(self, dist, visited):
        minimum = float('inf')
        index = -1
        for v in self.graph.keys():
            if visited[v] is False and dist[v] < minimum:
                minimum = dist[v]
                index = v

        return index

    def dikstra(self, src):
        visited = {i: False for i in self.graph}
        dist = {i: float('inf') for i in self.graph}

        dist[src] = 0

        for i in range(len(self.graph)-1):
            u = self.find_min(dist, visited)

            visited[u] = True
            for v, w in self.graph[u]:
                if visited[v] is False and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        return dist

    def printSolution(self, dist):

        for i in self.graph.keys():
            print(dist[i], end=' ')
        print()


T = int(input())

for t in range(T):
    N, K, X, M, S = list(map(int, input().split()))
    graph = Graph()
    for i in range(1, K+1):
        for j in range(i+1, K+1):
            if i != j:
                graph.addEdge(i, j, X)

    for m in range(M):
        a, b, c = list(map(int, input().split()))
        graph.addEdge(a, b, c)

    dist = graph.dikstra(S)
    graph.printSolution(dist)
