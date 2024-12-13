from functools import cache
from typing import NamedTuple
from util import *
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()


class Machine(NamedTuple):
    ax: int
    ay: int
    bx: int
    by: int
    px: int
    py: int


def parse_machine(s: str):
    ba, bb, p = s.splitlines()
    ax, ay = map(lambda x: int(x.split("+")[1]), ba.split(": ")[1].split(", "))
    bx, by = map(lambda x: int(x.split("+")[1]), bb.split(": ")[1].split(", "))
    px, py = map(lambda x: int(x.split("=")[1]), p.split(": ")[1].split(", "))
    return Machine(ax, ay, bx, by, px, py)


machine_strs = input.split("\n\n")
machines = [parse_machine(ms) for ms in machine_strs]


@cache
def mincost(m: Machine) -> tuple[bool, int]:
    new_mach = partial(Machine, m.ax, m.ay, m.bx, m.by)
    aok, bok = False, False
    if m.px == 0 and m.py == 0:
        return (True, 0)
    if m.ax <= m.px and m.ay <= m.py:
        aok, acost = mincost(new_mach(m.px - m.ax, m.py - m.ay))
    if m.bx <= m.px and m.by <= m.py:
        bok, bcost = mincost(new_mach(m.px - m.bx, m.py - m.by))
    if aok and bok:
        return (True, min(acost + 3, bcost + 1))
    if aok:
        return (True, acost + 3)
    if bok:
        return (True, bcost + 1)
    return (False, 0)


costs = []
for m in machines:
    ok, cost = mincost(m)
    if ok:
        costs.append(cost)
ans = sum(costs)

EXPECTED = 480

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
