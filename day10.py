import sys


def printarray(array):
    for row in array:
        print row


length = 256

with open(sys.argv[1], 'r') as fi:
    ring = range(0, length)
    ops = [int(s.strip(',')) for s in fi.readline().split(',')]
    i = 0
    step = 0
    for op in ops:
        if i + op >= length:
            shift = (i + op) % length
            sub = (ring[i:] + ring[0:shift])[::-1]
            ring = sub[-shift:] + ring[shift:i] + sub[0:op - shift]
        else:
            ring = ring[0:i] + ring[i:i + op][::-1] + ring[i + op:]
        i = (i + step + op) % length
        step += 1
    print ring
    print ring[0] * ring[1]
