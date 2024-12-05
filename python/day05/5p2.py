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


def topological_sort(graph):
    """
    graph: map of page -> pages that must come after it
    """
    dep_degree = {el: 0 for el in graph}

    # gen map of page to count of pages that need to come before it
    for page, reqs in graph.items():
        for req in reqs:
            dep_degree[req] += 1

    queue = deque(node for node in dep_degree if dep_degree[node] == 0)
    ordering = []

    while queue:
        page = queue.popleft()
        # if it's in the queue 0 pages need to come before it. Add to ordering
        ordering.append(page)
        for req in graph[page]:
            # we've added a page that needed to come before so decrement the count
            dep_degree[req] -= 1
            # add page if there isn't anything that needs to come before it
            if dep_degree[req] == 0:
                queue.append(req)

    assert len(ordering) == len(graph)
    return ordering


def process(input: str) -> int:
    ans = 0
    before = defaultdict(set)
    rules, orderings = input.split("\n\n")
    rules = parse_matrix(f=int, col_sep="|", s=rules)
    orderings = parse_matrix(f=int, col_sep=",", s=orderings)

    correct_ords = []
    incorrect_ords = []
    corrected_ords = []
    for rule in rules:
        before[rule[0]].add(rule[1])
    for ordering in orderings:
        seen = set()
        for page in ordering:
            seen.add(page)
            if before[page] & seen:
                incorrect_ords.append(ordering)
                break
        else:
            correct_ords.append(ordering)

    for ordering in incorrect_ords:
        dep_graph = {page: set(ordering) & before[page] for page in ordering}
        corrected_ords.append(topological_sort(dep_graph))

    for corrected_ord in corrected_ords:
        ans += corrected_ord[len(corrected_ord) // 2]
    return ans


EXPECTED = 123

print(f"expected: {EXPECTED}")
print(f"output: {process(input)}")
