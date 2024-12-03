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
    ans = 0
    mulexprs = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)
    for expr in mulexprs:
        operands = re.findall(r"\d{1,3}", expr)
        prod = mul(*[int(op) for op in operands])
        ans += prod
    return ans


EXPECTED = 161

print(f"expected: {EXPECTED}")
print(f"output: {process(input)}")
