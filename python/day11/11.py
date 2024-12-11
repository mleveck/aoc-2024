from util import *
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()

stones = list(map(int, lines[0].split()))

for _ in range(75):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue
        if len(str(stone)) % 2 == 0:
            sstr = str(stone)
            l = len(sstr)
            new_stones.append(int(sstr[: l // 2]))
            new_stones.append(int(sstr[l // 2 :]))
            continue
        new_stones.append(stone * 2024)
    stones = new_stones

ans = len(stones)

EXPECTED = 55312

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
