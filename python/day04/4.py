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
    lines = lines.copy()
    diagonals = []
    antidiagonals = []
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
    lines = list("".join(l) for l in zip(*reversed(lines)))
    for i in range(nrows):
        diagonal = ""
        for j in range(min(nrows - i, ncols)):
            diagonal += lines[i + j][j]
        antidiagonals.append(diagonal)
    for j in range(1, ncols):
        diagonal = ""
        for i in range(min(ncols - j, nrows)):
            diagonal += lines[i][i + j]
        antidiagonals.append(diagonal)
    return diagonals, antidiagonals


def process(input: str) -> int:
    ans = 0
    lines = input.splitlines()
    # horizontal
    for l in lines:
        ans += l.count("XMAS")
        ans += l[::-1].count("XMAS")
    # vertical
    flip = list("".join(l) for l in zip(*lines))
    for l in flip:
        ans += l.count("XMAS")
        ans += l[::-1].count("XMAS")
    # diagonals
    diag, antidiag = get_diag(lines)
    for l in diag:
        ans += l.count("XMAS")
        ans += l[::-1].count("XMAS")
    for l in antidiag:
        ans += l.count("XMAS")
        ans += l[::-1].count("XMAS")
    return ans


EXPECTED = 18

print(f"expected: {EXPECTED}")
print(f"output: {process(input)}")