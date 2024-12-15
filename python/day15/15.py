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

g, instructions = input.split("\n\n")
g = parse_matrix(s=g, col_sep="")
instructions = instructions.strip()
gmap = {(r, c): char for r, row in enumerate(g) for c, char in enumerate(row)}
rpos = [k for k, v in gmap.items() if v == "@"][0]
dirs = dict(zip("^v<>", [(-1, 0), (1, 0), (0, -1), (0, 1)]))


def gps(p: tuple[int, int]) -> int:
    return p[0] * 100 + p[1]


def trymove(source, dir) -> bool:
    assert source in gmap
    target = point_add(source, dir)
    assert target in gmap
    if gmap[target] == "#":
        return False
    if gmap[target] == ".":
        gmap[target] = gmap[source]
        gmap[source] = "."
        return True
    if gmap[target] == "O":
        ok = trymove(target, dir)
        if ok:
            gmap[target] = gmap[source]
            gmap[source] = "."
            return True


for step, inst in enumerate(instructions.replace("\n", "")):
    dir = dirs[inst]
    ok = trymove(rpos, dir)
    if ok:
        rpos = point_add(rpos, dir)


final_box_poss = [pos for pos, item in gmap.items() if item == "O"]
ans = sum(gps(pos) for pos in final_box_poss)
EXPECTED = 10092

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
