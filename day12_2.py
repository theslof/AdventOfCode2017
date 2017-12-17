import sys

def printarray(array):
    for row in array:
        print row


def contains(array, n):
    for i in array:
        for j in i:
            if j == n:
                return True
    return False


def visit(progs, groups, current):
    connections = progs[current]
    groups[-1] += [current]
    for v in connections:
        if contains(groups, v):
            continue
        else:
            groups[-1] += [v]
            visit(progs, groups, v)
    return groups + [[]]


with open(sys.argv[1], 'r') as fi:
    progs = []
    groups = [[]]
    current = 0
    for row in fi:
        data = map(int, row.replace(',', '').split()[2:])
        progs += [data]
    for i in range(0, len(progs)):
        groups = visit(progs, groups, i)
    print groups
