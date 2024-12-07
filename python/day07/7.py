from util import *
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()
calibrations = []


def can_equal(arg, rest, target):
    if not rest:
        return arg == target
    return (
        can_equal(arg + rest[0], rest[1:], target) or
        can_equal(arg * rest[0], rest[1:], target)
    )


for l in lines:
    res, args = l.split(": ")
    res = int(res)
    args = tuple(map(int, args.split()))
    calibrations.append((res, args))


ans = 0
for target, fargs in calibrations:
    if can_equal(fargs[0], fargs[1:], target):
        ans += target

EXPECTED = 3749

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
