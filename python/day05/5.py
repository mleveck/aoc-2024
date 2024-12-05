import re
from util import *
from collections import Counter, defaultdict, deque
from itertools import pairwise
import sys
from operator import mul

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()



def process(input: str) -> int:
    ans =0
    before = defaultdict(set)
    rules, orderings = input.split("\n\n")
    rules = parse_matrix(f=int, col_sep="|", s=rules)
    orderings= parse_matrix(f=int, col_sep=",", s=orderings)
    ans_ords = []
    for rule in rules:
        before[rule[0]].add(rule[1])
    for ordering in orderings:
        seen = set()
        for page in ordering:
            seen.add(page)
            if before[page] & seen:
                break
        else:
            ans_ords.append(ordering)

    for aord in ans_ords:
        print(aord)
        ans += aord[len(aord)//2]
    return ans


EXPECTED = 143

print(f"expected: {EXPECTED}")
print(f"output: {process(input)}")
