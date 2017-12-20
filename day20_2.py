# A really dirty implementation. It eliminates any colliding pixels each step, reducing the number of checks.
# Still far too many checks and loops, slow as hell (several seconds for 1000 loops).
# There must be some fancy mathematical solution to see if two vectors collide at time t, but vector algebra is not
# my strong suit and I should study for a test instead.

import sys


class Pixel:
    def __init__(self):
        self.coords = [0, 0, 0]
        self.v = [0, 0, 0]
        self.a = [0, 0, 0]

    def __str__(self):
        return '(' + str(self.coords[0]) + ',' + str(self.coords[1]) + ',' + str(self.coords[2]) + ')'


def step(pixel):
    for i in range(0, 3):
        pixel.v[i] += pixel.a[i]
        pixel.coords[i] += pixel.v[i]


def checkcollision(array):
    match = True
    while match:
        match = False
        for pixel in set(array):
            deadpixels = [p for p in array if p.coords == pixel.coords]
            if len(deadpixels) > 1:
                map(array.remove, deadpixels)
                match = True
                break


with open(sys.argv[1], 'r') as fi:
    data = set()
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
        data.add(p)
    #        print p
    l = len(data)
    print l
    for i in range(0, 1000):
        if len(data) <= 1:
            break
        checkcollision(data)
        map(step, data)
        if len(data) < l:
            l = len(data)
    print l
