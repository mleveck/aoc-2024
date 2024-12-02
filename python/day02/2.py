from util import *
from collections import Counter, deque
from itertools import pairwise
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()

safe = 0
for l in lines:
    l = map(int, l.split())
    pairs = list(pairwise(l))
    deltas = [p[1] - p[0] for p in pairs]
    if (all(d > 0 for d in deltas) or all(d < 0 for d in deltas)) and all(
        abs(d) > 0 and abs(d) < 4 for d in deltas
    ):
        print(deltas)
        safe += 1
print(safe)
