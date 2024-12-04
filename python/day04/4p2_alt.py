from util import point_add, parse_matrix
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()

grid = parse_matrix(col_sep="", s=input)
pos_map = {(r, c): char for r, col in enumerate(grid) for c, char in enumerate(col)}
diag1 = [(-1, -1), (1, 1)]
diag2 = [(1, -1), (-1, 1)]
valid_chars = {"MS", "SM"}

ans = 0
for pos, char in pos_map.items():
    if char != "A":
        continue
    d1 = "".join(pos_map.get(point_add(pos, dir), "OOB") for dir in diag1)
    d2 = "".join(pos_map.get(point_add(pos, dir), "OOB") for dir in diag2)
    if d1 in valid_chars and d2 in valid_chars:
        ans += 1

print(ans)
