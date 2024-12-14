from typing import NamedTuple
from util import *
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


def is_symmetric(s: set[int]) -> bool:
    l = list(sorted(s))
    if len(l) < 2:
        return False
    m = None
    if len(l) % 2 == 1:
        m = l[len(l) // 2]
    else:
        m = (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    left, right = 0, len(l) - 1
    while right > left:
        if ((l[right] - l[left]) / 2) + l[right] != m:
            return False
        right -= 1
        left += 1
    print(l, m)
    return True


for l in lines:
    p, v = l.split()
    p = p.split("=")[1].split(",")
    v = v.split("=")[1].split(",")
    p = tuple(map(int, p))
    v = tuple(map(int, v))
    robots.append(Robot(p, v))


def maybe_tree(r_poss):
    for MID in range(X):
        nonsymcount = 0
        for rpos in r_poss:
            d_from_mid = MID - rpos[0]
            if (MID + d_from_mid, rpos[1]) not in r_poss:
                nonsymcount += 1
            if nonsymcount > 0.3 * len(r_poss):
                break
        else:
            return True
    return False


def print_grid(r_poss, s):
    print(f"Step {s}:")
    for y in range(Y):
        l = "".join("x" if (x, y) in r_poss else "." for x in range(X))
        print(l)
    print("")


for s in range(1, 100000000):
    if s % 1000 == 0:
        print(f"Step {s}:")
    new_robot_poss = set()
    new_robots = []
    for robot in robots:
        xpos = (robot.p[0] + robot.v[0]) % X
        ypos = (robot.p[1] + robot.v[1]) % Y
        new_robot_poss.add((xpos, ypos))
        new_robots.append(Robot((xpos, ypos), robot.v))
    if maybe_tree(new_robot_poss):
        print_grid(new_robot_poss, s)
        break
    robots = new_robots
