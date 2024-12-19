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
towels, patterns = input.split("\n\n")
towels = towels.split(", ")
towels = tuple(towels)
patterns = patterns.splitlines()

@cache
def validate(pattern: str, towels: tuple[str]) -> bool:
    if not pattern:
        return True
    for towel in towels:
        if len(pattern) >= len(towel) and pattern.startswith(towel):
            if validate(pattern[len(towel):], towels):
                return True
    return False

valid = [validate(pattern, towels) for pattern in patterns]
ans = sum(valid)
EXPECTED = 6

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
