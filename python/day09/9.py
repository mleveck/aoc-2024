from typing import NamedTuple
from util import *
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

assert len(input) % 2 == 1
new_fblocks = []
fblocks = list(File(int(i), int(n)) for i, n in enumerate(input[::2]))
eblocks = list(int(n) for n in input[1::2])
nfblocks = sum(f.nblocks for f in fblocks)

blocks_iter = iter(fblocks)
rev_blocks = iter(reversed(fblocks))

rem_fblock_cnt = nfblocks
id, blocks = next(rev_blocks)
for empty_cnt in eblocks:
    remain = empty_cnt
    next_ord_block = next(blocks_iter)
    if rem_fblock_cnt <= next_ord_block.nblocks:
        new_fblocks.append(File(next_ord_block.id, rem_fblock_cnt))
        break
    new_fblocks.append(next_ord_block)
    rem_fblock_cnt -= next_ord_block.nblocks
    while remain > 0:
        if blocks > 0:
            allocate = min(blocks, remain, rem_fblock_cnt)
            new_block = File(id, allocate)
            new_fblocks.append(new_block)
            remain = remain - allocate
            blocks = blocks - allocate
            rem_fblock_cnt = rem_fblock_cnt - allocate
        else:
            id, blocks = next(rev_blocks)

idx = 0
checksum = 0
for fblock in new_fblocks:
    for n in range(fblock.nblocks):
        checksum += fblock.id * idx
        idx += 1


EXPECTED = 1928

print(f"expected: {EXPECTED}")
print(f"output: {checksum}")
