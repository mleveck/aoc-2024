from functools import *
from collections import *
from typing import NamedTuple
from util import *
from operator import add, mul
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()

#g = parse_matrix(s=g, col_sep="")
#gmap = {(r, c): char for r, row in enumerate(g) for c, char in enumerate(row)}

class Registers(NamedTuple):
    A: int
    B: int
    C: int

regs, prog = input.split("\n\n")

regs = Registers(*[int(l.split()[-1]) for l in regs.splitlines()])
prog = list(map(int, prog.split()[1].split(",")))

def compute(regs: Registers, program: list[int]):
    out = []
    a, b, c = regs
    ip = 0

    while ip < len(program) -1:
        opcode = program[ip]
        operand = program[ip + 1]
        combo_operand = operand
        if operand == 4:
            combo_operand = a
        if operand == 5:
            combo_operand = b
        if operand == 6:
            combo_operand = c

        print(f"{a=}, {b=}, C {c=}, IP {ip=}, {opcode=}, {operand=}, {out=}, {combo_operand=}")
        if opcode == 0:
            a = a//(2**combo_operand)
        if opcode == 1:
            b = b ^ operand
        if opcode == 2:
            b = combo_operand % 8
        if opcode == 3:
            if a != 0:
                ip = operand
                continue
        if opcode == 4:
            b = b ^ c
        if opcode == 5:
            out.append(combo_operand % 8)
        if opcode == 6:
            b = a//(2**combo_operand)
        if opcode == 7:
            c = a//(2**combo_operand)
        ip += 2
    return ",".join(map(str, out))




ans = compute(regs, prog)
EXPECTED = "4,6,3,5,6,3,5,2,1,0"

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
