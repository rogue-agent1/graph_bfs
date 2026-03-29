from graph_bfs import Graph
g = Graph()
for u, v in [(0,1),(0,2),(1,3),(2,3),(3,4)]:
    g.add_edge(u, v)
order = g.bfs(0)
assert order[0] == 0
assert set(order) == {0,1,2,3,4}
path = g.shortest_path(0, 4)
assert path[0] == 0 and path[-1] == 4
assert len(path) == 4  # 0->1->3->4 or 0->2->3->4
assert g.shortest_path(0, 99) is None
levels = g.level_order(0)
assert levels[0] == [0]
assert set(levels[1]) == {1, 2}
# Components
g2 = Graph()
g2.add_edge(0,1); g2.add_edge(2,3)
comps = g2.connected_components()
assert len(comps) == 2
print("graph_bfs tests passed")
