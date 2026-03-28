#!/usr/bin/env python3
"""Graph BFS/DFS — traversal, shortest path, components."""
import sys, json, collections
class Graph:
    def __init__(self): self.adj = collections.defaultdict(list)
    def add(self, u, v, w=1): self.adj[u].append((v,w)); self.adj[v].append((u,w))
    def bfs(self, start):
        visited = set(); q = collections.deque([start]); visited.add(start); order = []
        while q:
            node = q.popleft(); order.append(node)
            for nb, _ in self.adj[node]:
                if nb not in visited: visited.add(nb); q.append(nb)
        return order
    def dfs(self, start, visited=None):
        if visited is None: visited = set()
        visited.add(start); order = [start]
        for nb, _ in self.adj[start]:
            if nb not in visited: order.extend(self.dfs(nb, visited))
        return order
    def shortest_path(self, start, end):
        dist = {start: 0}; prev = {}; q = collections.deque([start])
        while q:
            node = q.popleft()
            for nb, w in self.adj[node]:
                if nb not in dist: dist[nb] = dist[node]+w; prev[nb] = node; q.append(nb)
        path = []; n = end
        while n in prev: path.append(n); n = prev[n]
        path.append(start); return list(reversed(path)), dist.get(end, -1)
    def components(self):
        visited = set(); comps = []
        for node in self.adj:
            if node not in visited:
                comp = self.bfs(node); visited.update(comp); comps.append(comp)
        return comps
def cli():
    g = Graph()
    edges = [("A","B"),("B","C"),("C","D"),("A","D"),("D","E"),("F","G")]
    for u,v in edges: g.add(u,v)
    print(f"  BFS from A: {g.bfs('A')}"); print(f"  DFS from A: {g.dfs('A')}")
    path, dist = g.shortest_path("A","E"); print(f"  Shortest A→E: {path} (dist={dist})")
    print(f"  Components: {g.components()}")
if __name__ == "__main__": cli()
