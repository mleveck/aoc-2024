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
    input = "do()" + input
    mulregex = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.finditer(mulregex, input)
    products = []
    for match in matches:
        mstart = match.start()
        do_index = input.rfind("do()", 0, mstart)
        dont_index = input.rfind("don't()", 0, mstart)
        if do_index > dont_index:
            products.append(int(match.group(1)) * int(match.group(2)))
    return sum(products)


EXPECTED = 48

print(f"expected: {EXPECTED}")
print(f"output: {process(input)}")
