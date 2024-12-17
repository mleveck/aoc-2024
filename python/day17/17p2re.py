from functools import *
from collections import *
from typing import NamedTuple
from util import *
from operator import add, mul
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed


class Registers(NamedTuple):
    A: int
    B: int
    C: int

def compute(regs: Registers, program: list[int], init: int):
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

        #print(f"{a=}, {b=}, C {c=}, IP {ip=}, {opcode=}, {operand=}, {out=}, {combo_operand=}")
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
    return out == program, init

def compute_range(start, end, regs, prog):
    for i in range(start, end):
        ok, aval = compute(Registers(i, regs.B, regs.C), prog, i)
        if ok:
            return (ok, aval)
    return False, 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = open(sys.argv[1]).read().strip()
    else:
        input = open("./sample.txt").read().strip()

    lines = input.splitlines()
    regs, prog = input.split("\n\n")

    regs = Registers(*[int(l.split()[-1]) for l in regs.splitlines()])
    prog = list(map(int, prog.split()[1].split(",")))

    a = 0
    with ProcessPoolExecutor() as executor:
        futs = []
        start = 2700000000

        not_found = True
        batch_size = 100_000_000
        ncores = 8
        while not_found:
            for i in range(ncores):
                sr = start + (batch_size * i)
                er = sr + batch_size
                print(f"submiting {sr=} {er=}")
                fut = executor.submit(compute_range, sr, er, regs, prog)
                futs.append(fut)
            for f in as_completed(futs):
                ok, aval = f.result()
                if ok:
                    print(f"good {aval=}")
                    not_found = False
                    break
            else:
                start  += ncores * batch_size
