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


def print_grid(grid):
    for row in grid:
        print("".join(row))


new_g = []
for r, row in enumerate(g):
    new_row = []
    for c, char in enumerate(row):
        if char == ".":
            new_row.append(".")
            new_row.append(".")
        if char == "#":
            new_row.append("#")
            new_row.append("#")
        if char == "@":
            new_row.append("@")
            new_row.append(".")
        if char == "O":
            new_row.append("[")
            new_row.append("]")
    new_g.append(new_row)
g = new_g


def print_gmap(gmap):
    for r in range(len(g)):
        l = ""
        for c in range(len(g[0])):
            l += gmap[(r, c)]
        print(l)


instructions = instructions.strip()
gmap = {(r, c): char for r, row in enumerate(g) for c, char in enumerate(row)}
rpos = [k for k, v in gmap.items() if v == "@"][0]
dirs = dict(zip("^v<>", [(-1, 0), (1, 0), (0, -1), (0, 1)]))


def gps(p: tuple[int, int]) -> int:
    return p[0] * 100 + p[1]


def trymove(source, dir) -> tuple[bool, list[tuple[tuple[int, int], tuple[int, int]]]]:
    assert source in gmap
    target = point_add(source, dir)
    assert target in gmap
    if gmap[target] == "#":
        return (False, [])
    if gmap[target] == ".":
        return True, [(source, target)]
    if gmap[target] in "[]":
        if dir in [dirs["<"], dirs[">"]]:
            ok, new_poss = trymove(target, dir)
            if ok:
                return (True, new_poss + [(source, target)])
            else:
                return (False, [])
        else:
            if gmap[target] == "[":
                buddy = point_add(target, (0, 1))
            elif gmap[target] == "]":
                buddy = point_add(target, (0, -1))
            buddyok, buddynewposs = trymove(buddy, dir)
            selfok, selfnewposs = trymove(target, dir)
            if buddyok and selfok:
                return (True, buddynewposs + selfnewposs + [(source, target)])
            else:
                return False, []
    assert (
        False
    ), f"Hit a condition unhandled move condition moving {source} {gmap[source]} to {target} {gmap[target]} in dir {dir}"


for step, inst in enumerate(instructions.replace("\n", "")):
    dir = dirs[inst]
    ok, new_poss = trymove(rpos, dir)
    if ok:
        sources = set()
        targets = set()
        assignments = []
        for source, target in new_poss:
            sources.add(source)
            targets.add(target)
            assignments.append((target, gmap[source]))
        for k, v in assignments:
            gmap[k] = v
        for source in sources:
            if source not in targets:
                gmap[source] = "."
        rpos = point_add(rpos, dir)

print_gmap(gmap)


final_box_poss = [pos for pos, item in gmap.items() if item == "["]
ans = sum(gps(pos) for pos in final_box_poss)
EXPECTED = 9021

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
