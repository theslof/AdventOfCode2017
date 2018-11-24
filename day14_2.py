from operator import xor
from functools import reduce


def knothash(string):
    length = 256
    ring = list(range(length))
    ops = [ord(c) for c in string] + [17, 31, 73, 47, 23]
    i = 0
    step = 0
    for _ in range(64):
        for op in ops:
            if i + op >= length:
                r = ring + ring
                r = r[0:i] + r[i:i + op][::-1] + r[i + op:]
                ring = r[length:i + op] + r[(i + op) % length:length]
            else:
                ring = ring[0:i] + ring[i:i + op][::-1] + ring[i + op:]
            i = (i + step + op) % length
            step += 1
    # '%02x' % <-- Format every element in list after % as a hex string
    #                 XOR all elements in list ring[n*16:n*16+16]
    return ''.join(['%02x' % reduce(xor, (x for x in ring[n*16:n*16+16])) for n in range(16)])


def stringtobin(string):
    return ''.join(["{0:04b}".format(int(c, 16)) for c in string])


def nukegrid(array, x, y):
    if x < 0 or x > 127 or y < 0 or y > 127 or array[x][y] == '0':
        return
    array[x][y] = '0'
    nukegrid(array, x - 1, y)
    nukegrid(array, x, y - 1)
    nukegrid(array, x + 1, y)
    nukegrid(array, x, y + 1)


data = open('day14.in', 'r').readline() + '-'
grid = [list(stringtobin(knothash(data + str(i)))) for i in range(128)]
groups = 0
for x in range(128):
    for y in range(128):
        if grid[x][y] == '0':
            continue
        groups += 1
        nukegrid(grid, x, y)

print(groups)
