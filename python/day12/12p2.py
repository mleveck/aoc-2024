from util import *
from collections import deque, defaultdict
import sys

if len(sys.argv) > 1:
    input = open(sys.argv[1]).read().strip()
else:
    input = open("./sample.txt").read().strip()

lines = input.splitlines()

g = parse_matrix(s=input, col_sep="")
gmap = {(r, c): char for r, row in enumerate(g) for c, char in enumerate(row)}

mapped = set()
regions = list()


def map_region(start, g):
    Q = deque([start])
    seen = set([start])
    region = []
    while Q:
        plot = Q.popleft()
        region.append(plot)
        neighbors = limited_potential_neighbors(plot[0], plot[1], g)
        reg_ns = {n for n in neighbors if gmap[n] == gmap[plot] and n not in seen}
        Q.extend(reg_ns)
        seen |= reg_ns
    return region


def area(region):
    return len(region)


def sides(region):
    sides = 0
    bare_row_to_plot = defaultdict(set)
    bare_col_to_plot = defaultdict(set)
    for plot in region:
        neighbors = set(
            n for n in limited_potential_neighbors(plot[0], plot[1]) if n in region
        )
        t, r, b, l = (-1, 0), (0, 1), (1, 0), (0, -1)
        top = point_add(plot, (-1, 0))
        right = point_add(plot, (0, 1))
        bottom = point_add(plot, (1, 0))
        left = point_add(plot, (0, -1))
        if top not in region:
            if not neighbors & bare_row_to_plot[top[0]]:
                sides += 1
                ln = point_add(plot, l)
                while ln in region:
                    if point_add(ln, t) in region:
                        break
                    bare_row_to_plot[top[0]].add(ln)
                    ln = point_add(ln, l)
                rn = point_add(plot, r)
                while rn in region:
                    if point_add(rn, t) in region:
                        break
                    bare_row_to_plot[top[0]].add(rn)
                    rn = point_add(rn, r)
            bare_row_to_plot[top[0]].add(plot)
        if right not in region:
            if not neighbors & bare_col_to_plot[right[1]]:
                sides += 1
                tn = point_add(plot, t)
                while tn in region:
                    if point_add(tn, r) in region:
                        break
                    bare_col_to_plot[right[1]].add(tn)
                    tn = point_add(tn, t)
                bn = point_add(plot, b)
                while bn in region:
                    if point_add(bn, r) in region:
                        break
                    bare_col_to_plot[right[1]].add(bn)
                    bn = point_add(bn, b)
            bare_col_to_plot[right[1]].add(plot)
        if bottom not in region:
            if not neighbors & bare_row_to_plot[bottom[0]]:
                sides += 1
                ln = point_add(plot, l)
                while ln in region:
                    if point_add(ln, b) in region:
                        break
                    bare_row_to_plot[bottom[0]].add(ln)
                    ln = point_add(ln, l)
                rn = point_add(plot, r)
                while rn in region:
                    if point_add(rn, b) in region:
                        break
                    bare_row_to_plot[bottom[0]].add(rn)
                    rn = point_add(rn, r)
            bare_row_to_plot[bottom[0]].add(plot)
        if left not in region:
            if not neighbors & bare_col_to_plot[left[1]]:
                sides += 1
                tn = point_add(plot, t)
                while tn in region:
                    if point_add(tn, l) in region:
                        break
                    bare_col_to_plot[left[1]].add(tn)
                    tn = point_add(tn, t)
                bn = point_add(plot, b)
                while bn in region:
                    if point_add(bn, l) in region:
                        break
                    bare_col_to_plot[left[1]].add(bn)
                    bn = point_add(bn, b)
            bare_col_to_plot[left[1]].add(plot)
    return sides


for plot in gmap:
    if plot not in mapped:
        region = map_region(plot, g)
        mapped |= set(region)
        regions.append(region)

prices = [area(r) * sides(r) for r in regions]
ans = sum(prices)

EXPECTED = 80

print(f"expected: {EXPECTED}")
print(f"output: {ans}")
