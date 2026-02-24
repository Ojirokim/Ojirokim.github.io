---
title: "Python Practice – Day 34"
date: 2026-02-24
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Instead of codeKata, studying the methods that will be used in the codekata.
- Data Structure & Algorithm

---

### DSA Tutorial
https://www.w3schools.com/dsa/dsa_intro.php

### Maximum Flow

#### 1. Terminology And Concepts
Flow network: A directed graph that represents a flow network.
Capacity: The maximum flow that can be transferred through a directed edge.
Source: The node from which the flow starts.
Sink: The node to which the flow ends.
Augmented path: Path where more flow can be transferred.
Residual network: Set up with the residual capacities on each edge, 
                where the residual capacity of an edge is the capacity on that edge, minus the flow.

#### 2. Max-flow Min-cut Theorem
The minimum cut is the cut we can make with the lowest total capacity, which will be the bottleneck.
The max-flow min-cut theorem says that finding the minimum cut in a graph, 
is the same as finding the maximum flow, because the value of the minimum cut will be the same value as the maximum flow.
If we want to increase flow beyond the maximum limit, which is often the case in practical situations, 
we now know which edges in the graph that needs to be modified to increase the overall flow.


#### 3. The Ford-Fulkerson Algorithm
The Ford-Fulkerson algorithm is a dynamic programming algorithm that finds the maximum flow in a flow network.
It works by repeatedly finding augmenting paths and adding the maximum flow to those paths.
To send flow back, in the opposite direction of the edge, 
a reverse edge is created for each original edge in the network. 
The Ford-Fulkerson algorithm can then use these reverse edges to send flow in the reverse direction.
```python
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, c):
        self.adj_matrix[u][v] = c

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def dfs(self, s, t, visited=None, path=None):
        if visited is None:
            visited = [False] * self.size
        if path is None:
            path = []

        visited[s] = True
        path.append(s)

        if s == t:
            return path

        for ind, val in enumerate(self.adj_matrix[s]):
            if not visited[ind] and val > 0:
                result_path = self.dfs(ind, t, visited, path.copy())
                if result_path:
                    return result_path
        return None
    def fordFulkerson(self, source, sink):
        max_flow = 0

        path = self.dfs(source, sink)
        while path:
            path_flow = float("Inf")
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                path_flow = min(path_flow, self.adj_matrix[u][v])

            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                self.adj_matrix[u][v] -= path_flow
                self.adj_matrix[v][u] += path_flow

            max_flow += path_flow

            path_names = [self.vertex_data[node] for node in path]
            print("Path:", " -> ".join(path_names), ", Flow:", path_flow)

            path = self.dfs(source, sink)
        return max_flow
g = Graph(6)
vertex_names = ['s', 'v1', 'v2', 'v3', 'v4', 't']
for i, name in enumerate(vertex_names):
    g.add_vertex_data(i, name)

g.add_edge(0, 1, 3)  # s  -> v1, cap: 3
g.add_edge(0, 2, 7)  # s  -> v2, cap: 7
g.add_edge(1, 3, 3)  # v1 -> v3, cap: 3
g.add_edge(1, 4, 4)  # v1 -> v4, cap: 4
g.add_edge(2, 1, 5)  # v2 -> v1, cap: 5
g.add_edge(2, 4, 3)  # v2 -> v4, cap: 3
g.add_edge(3, 4, 3)  # v3 -> v4, cap: 3
g.add_edge(3, 5, 2)  # v3 -> t,  cap: 2
g.add_edge(4, 5, 6)  # v4 -> t,  cap: 6
source = 0; sink = 5

print("The maximum possible flow is %d " % g.fordFulkerson(source, sink))
```

#### 4. The Ford-Fulkerson Algorithm
Similar to the Ford-Fulkerson algorithm, except the Edmonds-Karp algorithm 
uses Breadth First Search (BFS) to find augmented paths to increase flow.
```python
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, c):
        self.adj_matrix[u][v] = c

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def bfs(self, s, t, parent):
        visited = [False] * self.size
        queue = []  # Using list as a queue
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)  # Pop from the start of the list

            for ind, val in enumerate(self.adj_matrix[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return visited[t]

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.size
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.adj_matrix[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while(v != source):
                u = parent[v]
                self.adj_matrix[u][v] -= path_flow
                self.adj_matrix[v][u] += path_flow
                v = parent[v]

            path = []
            v = sink
            while(v != source):
                path.append(v)
                v = parent[v]
            path.append(source)
            path.reverse()
            path_names = [self.vertex_data[node] for node in path]
            print("Path:", " -> ".join(path_names), ", Flow:", path_flow)

        return max_flow

# Example usage:
g = Graph(6)
vertex_names = ['s', 'v1', 'v2', 'v3', 'v4', 't']
for i, name in enumerate(vertex_names):
    g.add_vertex_data(i, name)

g.add_edge(0, 1, 3)  # s  -> v1, cap: 3
g.add_edge(0, 2, 7)  # s  -> v2, cap: 7
g.add_edge(1, 3, 3)  # v1 -> v3, cap: 3
g.add_edge(1, 4, 4)  # v1 -> v4, cap: 4
g.add_edge(2, 1, 5)  # v2 -> v1, cap: 5
g.add_edge(2, 4, 3)  # v2 -> v4, cap: 3
g.add_edge(3, 4, 3)  # v3 -> v4, cap: 3
g.add_edge(3, 5, 2)  # v3 -> t,  cap: 2
g.add_edge(4, 5, 6)  # v4 -> t,  cap: 6

source = 0; sink = 5
print("The maximum possible flow is %d " % g.edmonds_karp(source, sink))

```