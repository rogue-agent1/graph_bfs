#!/usr/bin/env python3
"""BFS and DFS graph traversal."""
import sys, collections
g = collections.defaultdict(list)
for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) >= 2: g[parts[0]].append(parts[1]); g[parts[1]].append(parts[0])
start = sys.argv[1] if len(sys.argv) > 1 else next(iter(g), None)
if not start: sys.exit("No graph data")
mode = sys.argv[2] if len(sys.argv) > 2 else 'bfs'
visited, order = set(), []
if mode == 'bfs':
    q = collections.deque([start]); visited.add(start)
    while q:
        n = q.popleft(); order.append(n)
        for nb in g[n]:
            if nb not in visited: visited.add(nb); q.append(nb)
else:
    stack = [start]
    while stack:
        n = stack.pop()
        if n in visited: continue
        visited.add(n); order.append(n)
        for nb in reversed(g[n]): stack.append(nb)
print(' → '.join(order))
