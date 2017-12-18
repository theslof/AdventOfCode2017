import sys


def printarray(array):
    for row in array:
        print row


def knothash(string):
    length = 256
    dhash = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ring = range(0, length)
    ops = [ord(c) for c in string] + [17, 31, 73, 47, 23]
    i = 0
    step = 0
    for n in range(0, 64):
        for op in ops:
            if i + op >= length:
                r = ring + ring
                r = r[0:i] + r[i:i + op][::-1] + r[i + op:]
                ring = r[length:i + op] + r[(i + op) % length:length]
            else:
                ring = ring[0:i] + ring[i:i + op][::-1] + ring[i + op:]
            i = (i + step + op) % length
            step += 1
    for n in range(0, 16):
        for m in range(0, 16):
            dhash[n] = dhash[n] ^ ring[n * 16 + m]
    return ''.join(format(n, '02x') for n in dhash)


def stringtobin(string):
    return ''.join(["{0:04b}".format(int(c, 16)) for c in string])


with open(sys.argv[1], 'r') as fi:
    data = fi.readline() + '-'
    grid = [stringtobin(knothash(data + str(i))) for i in range(0, 128)]
    count = 0
    printarray(grid)
    for row in grid:
        for c in row:
            count += int(c)
    print count
