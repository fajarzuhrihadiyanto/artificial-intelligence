from node import Node
from graph import Graph

import matplotlib.pyplot as plt
import networkx as nx

graph1 = Graph()


bandar_lampung = Node('Bandar Lampung', 629)
jakarta = Node('Jakarta', 446)
bogor = Node('Bogor', 421)
bandung = Node('Bandung', 320)
cirebon = Node('Cirebon', 246)
tasikmalaya = Node('Tasikmalaya', 248)
purwokerto = Node('Purwokerto', 132)
cilacap = Node('Cilacap', 156)
semarang = Node('Semarang', 108)
yogyakarta = Node('Yogyakarta', 0)

graph1.add_edge(bandar_lampung, jakarta, 233)
graph1.add_edge(jakarta, bogor, 56)
graph1.add_edge(jakarta, cirebon, 219)
graph1.add_edge(bogor, bandung, 124)
graph1.add_edge(bandung, cirebon, 129)
graph1.add_edge(bandung, tasikmalaya, 111)
graph1.add_edge(tasikmalaya, cilacap, 144)
graph1.add_edge(cirebon, cilacap, 170)
graph1.add_edge(cirebon, purwokerto, 146)
graph1.add_edge(cirebon, semarang, 234)
graph1.add_edge(cilacap, purwokerto, 50)
graph1.add_edge(cilacap, yogyakarta, 172)
graph1.add_edge(purwokerto, yogyakarta, 168)
graph1.add_edge(semarang, yogyakarta, 130)

gbfs_cost, gbfs_path = graph1.gbfs(bandar_lampung, yogyakarta)
a_star_cost, a_star_path = graph1.a_star(bandar_lampung, yogyakarta)

G = nx.Graph()

pos = {
    bandar_lampung: (-4, 7),
    jakarta: (0, 4.5),
    cirebon: (8, 4),
    bogor: (0, 3),
    bandung: (5, 3),
    semarang: (15, 4),
    purwokerto: (11.5, 2),
    tasikmalaya: (7, 2),
    cilacap: (10, 1),
    yogyakarta: (16, 1)
}

for key, value in graph1.graph.items():
    for neighbour in value:
        G.add_edge(key, neighbour[0], weight=neighbour[1])

options = {
    "font_size": 8,
    "node_size": 1000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 2,
    "width": 2,
}
nx.draw_networkx(G, pos, **options)

ax = plt.gca()
ax.margins(0.10)
plt.axis("off")
plt.show()





