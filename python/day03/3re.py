import re
from util import *
from collections import Counter, deque
from itertools import pairwise
import sys
from operator import mul

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()


def process(input: str) -> int:
    products = []
    matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", input)
    for match in matches:
        products.append(int(match.group(1)) * int(match.group(2)))
    return sum(products)


EXPECTED = 161

print(f"expected: {EXPECTED}")
print(f"output: {process(input)}")
