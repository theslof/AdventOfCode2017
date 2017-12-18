import sys


def printarray(array):
    for row in array:
        print row


length = 256
dhash = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open(sys.argv[1], 'r') as fi:
    ring = range(0, length)
    ops = [ord(c) for c in [s for s in fi.readline()]] + [17, 31, 73, 47, 23]
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
    print ''.join([s[2:] for s in map(hex, dhash)])
