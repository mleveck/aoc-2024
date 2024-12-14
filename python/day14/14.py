import functools
from typing import NamedTuple
from util import *
from operator import mul
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()


class Robot(NamedTuple):
    p: tuple[int, int]
    v: tuple[int, int]


robots: list[Robot] = []

X = 101
Y = 103

for l in lines:
    p, v = l.split()
    p = p.split("=")[1].split(",")
    v = v.split("=")[1].split(",")
    p = tuple(map(int, p))
    v = tuple(map(int, v))
    robots.append(Robot(p, v))
quads = [0] * 4
for robot in robots:
    xpos = (robot.p[0] + 100 * robot.v[0]) % X
    ypos = (robot.p[1] + 100 * robot.v[1]) % Y
    if xpos in range(0, X // 2):
        if ypos in range(0, Y // 2):
            quads[0] += 1
        elif ypos in range(Y // 2 + 1, Y):
            quads[2] += 1
    elif xpos in range(X // 2 + 1, X):
        if ypos in range(0, Y // 2):
            quads[1] += 1
        elif ypos in range(Y // 2 + 1, Y):
            quads[3] += 1


ans = functools.reduce(mul, quads)

EXPECTED = 12

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
