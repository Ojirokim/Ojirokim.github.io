---
title: "Python Practice – Day 31"
date: 2026-02-19
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Instead of codeKata, studying the methods that will be used in the codekata.
- Data Structure & Algorithm

---

### DSA Tutorial
https://www.w3schools.com/dsa/dsa_intro.php

### 7. Graphs
A vertex, also called a node, is a point or an object in the Graph, 
and an edge is used to connect two vertices with each other.
A weighted Graph is a Graph where the edges have values. The weight value of an edge can represent things like distance, capacity, time, or probability.
A connected Graph is when all the vertices are connected through edges somehow. A Graph that is not connected, is a Graph with isolated (disjoint) subgraphs, or single isolated vertices.
A directed Graph, also known as a digraph, is when the edges between the vertex pairs have a direction. The direction of an edge can represent things like hierarchy or flow.
A cyclic Graph is defined differently depending on whether it is directed or not:
A directed cyclic Graph is when you can follow a path along the directed edges that goes in circles. Removing the directed edge from F to G in the animation above makes the directed Graph not cyclic anymore.
An undirected cyclic Graph is when you can come back to the same vertex you started at without using the same edge more than once. The undirected Graph above is cyclic because we can start and end up in vertes C without using the same edge twice.
A loop, also called a self-loop, is an edge that begins and ends on the same vertex. A loop is a cycle that only consists of one edge. By adding the loop on vertex A in the animation above, the Graph becomes cyclic.

```python
vertexData = ['A', 'B', 'C', 'D']

adjacency_matrix = [
    [0, 1, 1, 1],  # Edges for A
    [1, 0, 1, 0],  # Edges for B
    [1, 1, 0, 0],  # Edges for C
    [1, 0, 0, 0]   # Edges for D
]

def print_adjacency_matrix(matrix):
    print("\nAdjacency Matrix:")
    for row in matrix:
        print(row)

print('vertexData:',vertexData)
print_adjacency_matrix(adjacency_matrix)
```

```python
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size  

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1)  # A - B
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(1, 2)  # B - C
g.print_graph()
```