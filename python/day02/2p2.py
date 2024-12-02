from util import *
from collections import Counter, deque
from itertools import pairwise
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()


def validate(l):
    pairs = list(pairwise(l))
    deltas = [p[1] - p[0] for p in pairs]
    if (all(d > 0 for d in deltas) or all(d < 0 for d in deltas)) and all(
        abs(d) > 0 and abs(d) < 4 for d in deltas
    ):
        return True
    return False


safe = 0
for l in lines:
    l = list(map(int, l.split()))
    for i in range(len(l)):
        nl = l[0:i] + l[i + 1 :] # removing first/last level on safe list also safe
        if validate(nl):
            safe += 1
            break

print(safe)
