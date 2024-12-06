from os import walk
import re
from util import *
from collections import Counter, defaultdict, deque
from itertools import cycle, pairwise
import sys
from operator import getitem
import sys

sys.setrecursionlimit(15000)

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()
G = parse_matrix(s=input, col_sep="")
obstacles = set()
g_set = set()
right, down, left, up = (0, 1), (1, 0), (0, -1), (-1, 0)
guard_pos = None
for r, row in enumerate(G):
    for c, char in enumerate(row):
        g_set.add((r, c))
        if char == "#":
            obstacles.add((r, c))
        if char == "^":
            guard_pos = (r, c)
assert guard_pos
guard_start = guard_pos
ans = 0


def get_og_path(guard_dir, guard_pos):
    visited = set()
    dirs = cycle([right, down, left, up])
    while True:
        visited.add(guard_pos)
        new_pos = point_add(guard_pos, guard_dir)
        if new_pos not in g_set:
            return visited
        if new_pos in obstacles:
            guard_dir = next(dirs)
            continue
        guard_pos = new_pos


def causes_loop(guard_dir, guard_pos, obstacles):
    dirs = cycle([right, down, left, up])
    seen = set()
    while True:
        if (guard_pos, guard_dir) in seen:
            return True
        seen.add((guard_pos, guard_dir))
        new_pos = point_add(guard_pos, guard_dir)
        if new_pos not in g_set:
            return False
        if new_pos in obstacles:
            guard_dir = next(dirs)
            continue
        guard_pos = new_pos


og_path = get_og_path(up, guard_start)
for r, c in og_path:
    if (r, c) != guard_start:
        if causes_loop(up, guard_start, obstacles | {(r, c)}):
            ans += 1


EXPECTED = 6

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
