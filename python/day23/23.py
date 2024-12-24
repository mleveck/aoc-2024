from functools import *
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
    edges.add(frozenset((u,v)))


for u, v in edges:
    if "t" in {u[0], v[0]}:
        for node, adjset in graph.items():
            if node == v or  node == u:
                pass
            if {u, v}.issubset(adjset):
                triangles.add(frozenset([u, v, node]))

ans = len(triangles)
EXPECTED = 7

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
