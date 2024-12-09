from typing import NamedTuple
from util import *
from itertools import zip_longest
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()

G = parse_matrix(s=input, col_sep="")
points = set()
ans = 0


class File(NamedTuple):
    id: int
    nblocks: int


fidx_map = dict()
eidx_map = dict()
fblocks = list(File(int(i), int(n)) for i, n in enumerate(input[::2]))
eblocks = list(int(n) for n in input[1::2])
idx = 0

new_fidx_map = dict()

for file, empty in zip_longest(fblocks, eblocks):
    fidx_map[idx] = file
    idx += file.nblocks
    if empty != None:
        eidx_map[idx] = empty
        idx += empty

for fidx, file in reversed(sorted(fidx_map.items())):
    for eidx, empty_cnt in sorted(eidx_map.items()):
        if eidx >= fidx:
            new_fidx_map[fidx] = file
            break
        if empty_cnt >= file.nblocks:
            del eidx_map[eidx]
            new_fidx_map[eidx] = file
            if empty_cnt > file.nblocks:
                eidx_map[eidx + file.nblocks] = empty_cnt - file.nblocks
            break
checksum = 0
for fidx, file in new_fidx_map.items():
    for i in range(file.nblocks):
        checksum += file.id * (fidx + i)

EXPECTED = 2858

print(f"expected: {EXPECTED}")
print(f"output: {checksum}")
