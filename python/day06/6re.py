from os import walk
import re
from util import *
from collections import Counter, defaultdict, deque
from itertools import cycle, pairwise
import sys
from operator import mul

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()
G = parse_matrix(s=input, col_sep="")
obstacles = set()
g_set = set()
right, down, left, up = (0, 1), (1, 0), (0, -1), (-1, 0)
dirs = cycle([right, down, left, up])
guard_pos= None
for r, row in enumerate(G):
    for c, char in enumerate(row):
        g_set.add((r, c))
        if char == "#":
            obstacles.add((r, c))
        if char == "^":
            guard_pos = (r, c)
assert guard_pos
visited = set()

guard_dir = up

while(True):
    visited.add(guard_pos)
    new_pos = point_add(guard_pos, guard_dir)
    if new_pos not in g_set:
        break
    if new_pos in obstacles:
        guard_dir = next(dirs)
        continue
    guard_pos = new_pos

ans= len(visited)



EXPECTED = 41

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
