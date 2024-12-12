from util import *
from collections import deque
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()

g = parse_matrix(s=input, col_sep="")
gmap = {(r, c): char for r, row in enumerate(g) for c, char in enumerate(row)}

mapped = set()
regions = list()


def map_region(start, g):
    Q = deque([start])
    seen = set([start])
    while Q:
        plot = Q.popleft()
        neighbors = limited_potential_neighbors(plot[0], plot[1], g)
        reg_ns = {n for n in neighbors if gmap[n] == gmap[plot] and n not in seen}
        Q.extend(reg_ns)
        seen |= reg_ns
    return seen


def area(region):
    return len(region)


def perimeter(region):
    perim = 0
    for plot in region:
        neighbors = [
            n for n in limited_potential_neighbors(plot[0], plot[1], g) if n in region
        ]
        perim += 4 - len(neighbors)
    return perim


for plot in gmap:
    if plot not in mapped:
        region = map_region(plot, g)
        mapped |= region
        regions.append(region)

prices = [perimeter(r)*area(r) for r in regions]
ans = sum(prices)

EXPECTED = 140

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
