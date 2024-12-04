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


def process(input: str) -> int:
    ans = 0
    grid = parse_matrix(col_sep="", s=input)
    nrows = len(grid)
    ncols = len(grid[0])
    for rowi in range(1, nrows - 1):
        for coli in range(1, ncols - 1):
            char = grid[rowi][coli]
            if char == "A":
                if (
                    (
                        grid[rowi - 1][coli + 1] == "M"
                        and grid[rowi + 1][coli - 1] == "S"
                    )
                    or (
                        grid[rowi - 1][coli + 1] == "S"
                        and grid[rowi + 1][coli - 1] == "M"
                    )
                ) and (
                    (
                        grid[rowi - 1][coli - 1] == "M"
                        and grid[rowi + 1][coli + 1] == "S"
                    )
                    or (
                        grid[rowi - 1][coli - 1] == "S"
                        and grid[rowi + 1][coli + 1] == "M"
                    )
                ):
                    ans += 1
    return ans


EXPECTED = 9

print(f"expected: {EXPECTED}")
print(f"output: {process(input)}")
