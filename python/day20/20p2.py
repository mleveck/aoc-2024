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
g = parse_matrix(s=input, col_sep="")
gmap = {(r, c): char for r, row in enumerate(g) for c, char in enumerate(row)}
empty = {k: v for k, v in gmap.items() if v in ".SE"}
walls = {k: v for k, v in gmap.items() if v in "#"}
start = [k for k, v in empty.items() if v == "S"][0]
end = [k for k, v in empty.items() if v == "E"][0]

pos2dist: dict[tuple[int, int], int] = dict()
Q = deque([(end, 0)])
seen = set()
while Q:
    pos, dist = Q.popleft()
    if pos in seen:
        continue
    seen.add(pos)
    pos2dist[pos] = dist
    for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if (new_pos := point_add(dir, pos)) in empty:
            Q.append((new_pos, dist + 1))
dist2pos = defaultdict(set)

for pos, dist in pos2dist.items():
    dist2pos[dist].add(pos)


def neighbors(p1):
    ns = []
    adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dir in adj:
        if (n := point_add(dir, p1)) in gmap:
            ns.append(n)
    return ns


def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


cheats = dict()
thresh = 100
d2ps = sorted(dist2pos.items())

for pos, dist in pos2dist.items():
    potentialposs = set()
    for dist2, pps in d2ps:
        if dist2 >= dist + thresh:
            break
        for pp in pps:
            if (md := manhattan_dist(pos, pp)) < 21:
                if dist - (md + dist2) >= thresh:
                    cheats[(pos, pp)] = dist - (dist2 + md)
ans = len(cheats)
print(f"output: {ans}")
