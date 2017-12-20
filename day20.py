import sys, math


class Pixel:
    def __init__(self):
        self.coords = [0, 0, 0]
        self.v = [0, 0, 0]
        self.a = [0, 0, 0]


def manhattan(steps, c, v, a):
    cx = c[0] + steps * (v[0] + steps * a[0])
    cy = c[1] + steps * (v[1] + steps * a[1])
    cz = c[2] + steps * (v[2] + steps * a[2])
    return int(math.fabs(cx) + math.fabs(cy) + math.fabs(cz))


with open(sys.argv[1], 'r') as fi:
    data = list()
    i = 0
    for row in fi:
        p = Pixel()
        start = row.index('<')
        end = row.index('>')
        p.coords = map(int, row[start + 1:end].split(','))
        start = row[end:].index('<') + end
        end = row[start:].index('>') + start
        p.v = map(int, row[start + 1:end].split(','))
        start = row[end:].index('<') + end
        end = row[start:].index('>') + start
        p.a = map(int, row[start + 1:end].split(','))
        data.append([i, p, manhattan(1000000000, p.coords, p.v, p.a)])
        i += 1

    dist = [p[2] for p in data]
    i = dist.index(min(dist))
    print i
