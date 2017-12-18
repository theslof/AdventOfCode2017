import sys


def printarray(array):
    for row in array:
        print row


length = 256

with open(sys.argv[1], 'r') as fi:
    ring = range(0, length)
    ops = [int(s) for s in fi.readline().split(',')]
    i = 0
    step = 0
    for op in ops:
        if i + op >= length:
            r = ring + ring
            r = r[0:i] + r[i:i + op][::-1] + r[i + op:]
            ring = r[length:i + op] + r[(i + op) % length:length]
        else:
            ring = ring[0:i] + ring[i:i + op][::-1] + ring[i + op:]
        i = (i + step + op) % length
        step += 1
    print ring[0] * ring[1]
