from operator import xor
from functools import reduce

length = 256

with open('day10_data', 'r') as fi:
    ring = list(range(length))
    ops = [ord(c) for c in [s for s in fi.readline()]] + [17, 31, 73, 47, 23]
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
    dhash = ['%02x' % reduce(xor, (x for x in ring[n*16:n*16+16])) for n in range(16)]
    print(''.join(dhash))
