import util
from util import *
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()

G = parse_matrix(s=input, col_sep="", f=int)
GMAP = {(r, c): num for r, row in enumerate(G) for c, num in enumerate(row)}
theads = {p for p, num in GMAP.items() if num == 0}


def dfs(start):
    stack = [start]
    reachable = set()
    while stack:
        pos = stack.pop()
        if GMAP[pos] == 9:
            reachable.add(pos)
            continue
        neighbors = util.limited_potential_neighbors(pos[0], pos[1], G)
        for neighbor in neighbors:
            if GMAP[neighbor] - GMAP[pos] == 1:
                stack.append(neighbor)
    return len(reachable)


ans = 0
ans = sum(dfs(thead) for thead in theads)

EXPECTED = 36

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
