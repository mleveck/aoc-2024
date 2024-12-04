import re
from util import point_add, point_scale, parse_matrix, dydx
from collections import Counter, deque
from itertools import pairwise
import sys
from operator import mul

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()

grid = parse_matrix(col_sep="", s=input)
pos_map = {(r, c): char for r, col in enumerate(grid) for c, char in enumerate(col)}
dirs = dydx

ans = 0
for pos in pos_map:
    for dir in dirs:
        for i, target_char in enumerate("XMAS"):
            curr_pos = point_add(pos , point_scale(dir, i))
            if curr_pos not in pos_map or pos_map[curr_pos] != target_char:
                break
        else:
            ans += 1
print(ans)
