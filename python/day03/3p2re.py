import re
from util import *
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()


def process(input: str) -> int:
    mulregex = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"
    matches = re.findall(mulregex, input)
    products = []
    process = True
    for op1, op2, do, dont in matches:
        if do:
            process = True
            continue
        if dont:
            process = False
            continue
        if process:
            products.append(int(op1) * int(op2))

    return sum(products)


EXPECTED = 48

print(f"expected: {EXPECTED}")
print(f"output: {process(input)}")
