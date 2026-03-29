#!/usr/bin/env python3
"""BFS graph traversal. Zero dependencies."""
from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.adj = {}
        self.directed = directed

    def add_edge(self, u, v, weight=1):
        self.adj.setdefault(u, []).append((v, weight))
        if not self.directed:
            self.adj.setdefault(v, []).append((u, weight))

    def bfs(self, start):
        visited = set([start])
        queue = deque([start])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor, _ in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def shortest_path(self, start, end):
        if start == end: return [start]
        visited = {start}
        queue = deque([(start, [start])])
        while queue:
            node, path = queue.popleft()
            for neighbor, _ in self.adj.get(node, []):
                if neighbor == end: return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    def connected_components(self):
        visited = set()
        components = []
        for node in self.adj:
            if node not in visited:
                comp = self.bfs(node)
                visited.update(comp)
                components.append(comp)
        return components

    def level_order(self, start):
        visited = {start}
        queue = deque([(start, 0)])
        levels = {}
        while queue:
            node, lvl = queue.popleft()
            levels.setdefault(lvl, []).append(node)
            for neighbor, _ in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, lvl + 1))
        return levels

if __name__ == "__main__":
    g = Graph()
    for u, v in [(0,1),(0,2),(1,3),(2,3),(3,4)]:
        g.add_edge(u, v)
    print("BFS:", g.bfs(0))
    print("Path 0->4:", g.shortest_path(0, 4))
