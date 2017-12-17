import sys

def printarray(array):
    for row in array:
        print row


def contains(array, n):
    for i in array:
        if i == n:
            return True
    return False


def visit(progs, visited, current):
    c = 1
    connections = progs[current]
    for v in progs[current]:
        if contains(visited, v):
            continue
        else:
            c += visit(progs, visited + connections, v)
    return c


with open(sys.argv[1], 'r') as fi:
    progs = []
    current = 0
    for row in fi:
        data = map(int, row.replace(',', '').split()[2:])
        progs += [data]
    print visit(progs, [0], current)
