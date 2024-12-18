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

X = 71
Y = 71
mypos = (0, 0)

byte_poss = []
for l in lines:
    byte_poss.append(tuple(map(int, l.split(","))))

byte_poss

firstn = set(byte_poss[:1024])

seen = set()
Q = deque([(mypos, 0)])

while(Q):
    pos, cur_cost = Q.popleft()
    if pos in seen: continue
    seen.add(pos)
    if pos == (X -1, Y - 1):
        print(cur_cost)
        break
    for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        newp = point_add(dir, pos)
        if newp[0] in range(0, X) and newp[1] in range(0, Y) and newp not in firstn:
            Q.append((newp, cur_cost + 1))



ans = 0
EXPECTED = 22

print(f"expected: {EXPECTED}")
#print(f"output: {ans}")
