from util import *
from collections import Counter
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()

# part 1
l1, l2 = [], []
for l in lines:
    i1, i2 = l.split()
    l1.append(int(i1))
    l2.append(int(i2))
l1s = sorted(l1)
l2s = sorted(l2)
pairs = zip(l1s, l2s)
diffs = [abs(p[1] - p[0]) for p in pairs]
print(l1s)
print(l2s)
print(diffs)
print(sum(diffs))

# part 2
c2 = Counter(l2)
ans = 0
for id in l1:
    if id in c2:
        ans += id * c2.get(id)
print(ans)
