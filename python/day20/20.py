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

distances: dict[tuple[int, int], int] = dict()
Q = deque([(end, 0)])
seen = set()
while Q:
    pos, dist = Q.popleft()
    if pos in seen:
        continue
    seen.add(pos)
    distances[pos] = dist
    for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if (new_pos := point_add(dir, pos)) in empty:
            Q.append((new_pos, dist + 1))


def neighbors(p1):
    ns = []
    adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dir in adj:
        if (n := point_add(dir, p1)) in gmap:
            ns.append(n)
    return ns


saved = dict()

for pos, dist in distances.items():
    adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    wallns = [n for n in neighbors(pos) if n in walls]
    short_ends = set()
    for walln in wallns:
        owallns = set(n for n in neighbors(walln) if n in walls)
        short_ends |= set(n for n in neighbors(walln) if n in empty)
    short_ends = short_ends - {pos}
    for sc_end in short_ends:
        if distances[sc_end] + 2 < distances[pos]:
            saved[(pos, sc_end)] = distances[pos] - (distances[sc_end] + 2)

savings_counts = defaultdict(int)
for cheat, savings in saved.items():
    savings_counts[savings] += 1

ans = 0
for sec_savings, count in savings_counts.items():
    if sec_savings >= 100:
        ans += count
EXPECTED = 84

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
