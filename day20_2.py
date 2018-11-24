# A really dirty implementation. It eliminates any colliding pixels each step, reducing the number of checks.
# Slow and clunky, but I implemented a bail-out counter. If no collisions have been detected for n iterations, quit.
import re

bailout = 20


class Pixel:
    def __init__(self):
        self.coords = [0, 0, 0]
        self.v = [0, 0, 0]
        self.a = [0, 0, 0]

    def __str__(self):
        return '<' + str(self.coords[0]) + ',' + str(self.coords[1]) + ',' + str(self.coords[2]) + '>' \
              ' <' + str(self.v[0]) + ',' + str(self.v[1]) + ',' + str(self.v[2]) + '>' \
              ' <' + str(self.a[0]) + ',' + str(self.a[1]) + ',' + str(self.a[2]) + '>'


def step(data: [Pixel]):
    for pixel in data:
        for i in range(3):
            pixel.v[i] += pixel.a[i]
            pixel.coords[i] += pixel.v[i]


def checkcollision(array: {Pixel}):
    deadpixels = set()
    for index, pixel in enumerate(array):
        for p in array:
            if p.coords == pixel.coords and p != pixel:
                deadpixels.add(p)
    return deadpixels


with open('day20_data', 'r') as fi:
    data = set()
    for row in fi:
        p = Pixel()
        pl, vl, al, *_ = re.findall('<(.*?)>', row)
        p.coords = list(map(int, pl.split(',')))
        p.v = list(map(int, vl.split(',')))
        p.a = list(map(int, al.split(',')))
        data.add(p)
    print('Checking collisions...')
    i = 0
    for _ in range(10000):
        dead = checkcollision(data)
        if len(dead):
            data -= dead
            i = 0
        else:
            i += 1
        if i > bailout:
            break
        step(data)
    print(len(data))
