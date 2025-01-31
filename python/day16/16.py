from functools import *
from collections import *
from typing import NamedTuple
from util import *
import heapq
from operator import mul, add
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

def dijkstra(start, graph):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)

        for weight, neighbor in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances


lines = input.splitlines()
g = parse_matrix(s=input, col_sep="")
gmap = {(r, c): char for r, row in enumerate(g) for c, char in enumerate(row)}
start = [k for k,v in gmap.items() if v == "S"][0]
end = [k for k,v in gmap.items() if v == "E"][0]
open_spaces = {k for k,v in gmap.items() if v == "."}
open_spaces.add(start)
open_spaces.add(end)


def pnexts(p, facing):
    next_cells = []
    dr, dc = facing
    if (ahead := point_add(p, facing)) in open_spaces:
        next_cells.append((1, (ahead, facing)))
    for dir in [(dc, dr), (-dc, -dr)]:
        if (n := point_add(dir, p)) in open_spaces:
            next_cells.append((1001, (n, dir)))
    return next_cells

graph = dict()

for p in open_spaces:
    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        graph[(p, d)] = pnexts(p, d)
 
distances = dijkstra((start, (0, 1)), graph)

edists = [val for k, val in distances.items() if k[0] == end]


ans = min(edists)
EXPECTED = 7036
print(f"expected: {EXPECTED}")
print(f"output: {ans}")
