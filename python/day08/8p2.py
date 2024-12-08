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
points = set()
antenna2loc = defaultdict(list)

for r, row in enumerate(G):
    for c, char in enumerate(row):
        if char.isalnum():
            antenna2loc[char].append((c, r))
        points.add((c, r))

antinodes = set()
for _, tlocs in antenna2loc.items():
    tpairs = combinations(tlocs, 2)
    for t1, t2 in tpairs:
        og_t1, og_t2 = t1, t2
        rise = t2[1] - t1[1]
        run = t2[0] - t1[0]

        antinodes.add(t1)
        while (t1 := point_add(t1, (run, rise))) in points:
            antinodes.add(t1)

        t1 = og_t1
        while (t1 := point_add(t1, point_inv((run, rise)))) in points:
            antinodes.add(t1)

ans = len(antinodes)




EXPECTED = 34

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
