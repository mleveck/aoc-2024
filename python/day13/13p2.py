from typing import NamedTuple
from util import *
import sys
from z3 import Int, Optimize, sat

sys.setrecursionlimit(10000)

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

def mincost(mach: Machine) -> tuple[bool, int | None]:
    m = Int("m")
    n = Int("n")
    o = Optimize()
    o.add(m * mach.ax + n * mach.bx == mach.px)
    o.add(m * mach.ay + n * mach.by == mach.py)
    o.minimize(m*3 + n)
    cost = None
    ok = False
    if o.check() == sat:
        model = o.model()
        ok = True
        cost = model.evaluate(m*3 + n).as_long()
    return (ok, cost)

costs = []
BIG = 10000000000000
for i, m in enumerate(machines):
    print(f"processing {m=}")
    m = Machine(m.ax, m.ay, m.bx, m.by, m.px + BIG, m.py + BIG)
    ok, cost = mincost(m)
    if ok:
        print(f"solution for {i=}")
        costs.append(cost)
ans = sum(costs)

print(f"output: {ans}")
