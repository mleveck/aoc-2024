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
row_obs = defaultdict(list)
col_obs = defaultdict(list)
up, right, down, left = (-1, 0), (0, 1), (1, 0), (0, -1)
dirs = [up, right, down, left]
guard_pos= None
for r, row in enumerate(G):
    for c, char in enumerate(row):
        if char == "#":
            row_obs[r].append(c)
            col_obs[c].append(r)
        if char == "^":
            guard_pos = (r, c)

for row, alley in row_obs.items():
    alley.sort()

for col, alley in col_obs.items():
    alley.sort()

guard_dir = up

print(row_obs)

traveled_len = 0
for dir in cycle(dirs):
    if dir == up:
        alley_obs = col_obs[guard_pos[1]]
        for obs in alley_obs[::-1]:
            if obs < guard_pos[0]:
                new_guard_pos = (obs + 1, guard_pos[1])
                traveled_len += guard_pos[0] - obs
                break
        else:
            traveled_len += guard_pos[0]
            break
    if dir == down:
        alley_obs = col_obs[guard_pos[1]]
        for obs in alley_obs:
            if obs > guard_pos[0]:
                new_guard_pos = (obs - 1, guard_pos[1])
                traveled_len +=  obs - guard_pos[0]
                break
        else:
            traveled_len += len(G) - guard_pos[0]
            break
    if dir == right:
        alley_obs = row_obs[guard_pos[0]]
        for obs in alley_obs:
            if obs > guard_pos[1]:
                new_guard_pos = (guard_pos[0], obs - 1)
                traveled_len += obs - guard_pos[1]
                break
        else:
            traveled_len += len(G[0]) - guard_pos[1]
            break
    if dir == left:
        alley_obs = row_obs[guard_pos[0]]
        for obs in alley_obs[::-1]:
            if obs < guard_pos[1]:
                guard_pos = (guard_pos[0], obs + 1)
                traveled_len += guard_pos[1] - obs
                break
        else:
            traveled_len += guard_pos[1]
            break




ans= traveled_len



EXPECTED = 0

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
