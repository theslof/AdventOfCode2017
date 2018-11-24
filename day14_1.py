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
    return ['%02x' % reduce(xor, (x for x in ring[n*16:n*16+16])) for n in range(16)]


data = open('day14.in', 'r').readline() + '-'
print(sum(
    [len(
        # Get knothash data, convert to binary and drop zeroes
        # Return character x from binary representation of character c from knothash of data, only if x == 1
        # Input string -> knot hash (hex) -> binary -> only ones -> count length -> sum of length of all 128 rows
        [x for c in knothash(data + str(i)) for x in "{0:04b}".format(int(c, 16)) if x == '1']
    ) for i in list(range(128))]))
