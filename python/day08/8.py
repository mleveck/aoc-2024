from util import *
from collections import defaultdict
from itertools import combinations
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()

G = parse_matrix(s=input, col_sep="")
R = len(G)
C = len(G[0])
points = set()
loc2antannae = dict()
antenna2loc = defaultdict(list)

for r, row in enumerate(G):
    for c, char in enumerate(row):
        if char.isalnum():
            loc2antannae[(c, r)] = char
            antenna2loc[char].append((c, r))
        points.add((c, r))

antinodes = set()

for _, tlocs in antenna2loc.items():
    tpairs = combinations(tlocs, 2)
    for t1, t2 in tpairs:
        rise = t2[1] - t1[1]
        run = t2[0] - t1[0]
        if (pp := point_add(t2, (run, rise))) in points:
            antinodes.add(pp)

        if (pp2 := point_add(t1, point_inv((run, rise)))) in points:
            antinodes.add(pp2)

ans = len(antinodes)




EXPECTED = 14

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
