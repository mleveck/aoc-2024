from functools import *
from collections import *
import operator
from typing import NamedTuple
from itertools import *
from util import *
from operator import mul, add
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lks = input.split("\n\n")
keys, locks = set(), set()

for lk in lks:
    g = parse_matrix(s=lk, col_sep="")
    gt = list(zip(*g[::-1]))
    counts = tuple(r.count("#") for r in gt)
    if all(c == "#" for c in g[0]):
        locks.add(counts)
    else:
        keys.add(counts)

ans = 0
combos = list(product(keys, locks))
for combo in combos:
    if all(add(*pair) < 8 for pair in zip(*combo)):
        ans += 1


EXPECTED = 3

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
