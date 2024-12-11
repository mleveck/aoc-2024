from functools import cache
from util import *
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()

stones = list(map(int, lines[0].split()))


@cache
def transform(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return transform(1, blinks - 1)
    if len(str(stone)) % 2 == 0:
        sstr = str(stone)
        l = len(sstr)
        return (
            transform(int(sstr[: l // 2]), blinks - 1) + 
            transform(int(sstr[l // 2 :]), blinks - 1)
        )
    return transform(stone * 2024, blinks - 1)


ans = sum(transform(stone, 75) for stone in stones)

EXPECTED = 55312

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
