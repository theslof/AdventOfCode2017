from collections import Counter


def dist(x, y):
    return int((abs(x) + abs(y) + abs(x + y)) / 2)


opposites = [('n', 's'), ('ne', 'sw'), ('nw', 'se')]

with open('day11.in', 'r') as fi:
    data = fi.readline().split(',')
    x = 0
    y = 0
    maxdist = 0
    for step in data:
        maxdist = max(maxdist, dist(x, y))
        if step == 'n':
            y += 1
        elif step == 's':
            y -= 1
        elif step == 'ne':
            x += 1
        elif step == 'sw':
            x -= 1
        elif step == 'nw':
            y += 1
            x -= 1
        elif step == 'se':
            y -= 1
            x += 1
    print('11.1: ' + str(dist(x, y)))
    print('11.2: ' + str(maxdist))
