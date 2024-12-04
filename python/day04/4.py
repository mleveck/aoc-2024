import re
from util import *
from collections import Counter, deque
from itertools import pairwise
import sys
from operator import mul

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()


def get_diag(lines):
    diagonals = []
    nrows = len(lines)
    ncols = len(lines[0])
    for i in range(nrows):
        diagonal = ""
        for j in range(min(nrows - i, ncols)):
            diagonal += lines[i + j][j]
        diagonals.append(diagonal)
    for j in range(1, ncols):
        diagonal = ""
        for i in range(min(ncols - j, nrows)):
            diagonal += lines[i][i + j]
        diagonals.append(diagonal)
    return diagonals

def count_xmas(lines):
    ans = 0
    for l in lines:
        ans += l.count("XMAS")
        ans += l[::-1].count("XMAS")
    return ans


def process(input: str) -> int:
    lines = input.splitlines()
    flip = list("".join(l) for l in zip(*reversed(lines)))
    diag = get_diag(lines)
    antidiag = get_diag(flip)
    return sum(map(count_xmas, [lines, flip, diag, antidiag]))


EXPECTED = 18

print(f"expected: {EXPECTED}")
print(f"output: {process(input)}")
