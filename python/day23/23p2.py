from functools import *
import networkx as nx
from collections import *
from typing import NamedTuple
from util import *
from operator import mul, add
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()

graph = defaultdict(set)
edges = set()
triangles = set()
for l in lines:
    (u, v) = l.split("-")
    graph[u].add(v)
    graph[v].add(u)
    edges.add((u,v))
G = nx.Graph()
G.add_nodes_from(graph.keys())
G.add_edges_from(edges)
cliques = list(nx.find_cliques(G))
largest_clique = max(cliques, key=len)

ans = ",".join(sorted(largest_clique))
EXPECTED = "co,de,ka,ta"

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
