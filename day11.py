import sys
import math


def dist(x, y):
    return int((math.fabs(x) + math.fabs(y) + math.fabs(x + y)) / 2)


with open(sys.argv[1], 'r') as fi:
    data = fi.readline().split(',')
    x = 0
    y = 0
    maxdist = 0
    for step in data:
        maxdist = max(maxdist, dist(x, y))
        if step == 'n':
            y += 1
            continue
        if step == 's':
            y -= 1
            continue
        if step == 'ne':
            x += 1
            continue
        if step == 'sw':
            x -= 1
            continue
        if step == 'nw':
            y += 1
            x -= 1
            continue
        if step == 'se':
            y -= 1
            x += 1
            continue
    print dist(x, y)
    print maxdist
