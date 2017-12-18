# Supply the two starting values via a file, A's value on row 1, B's value on row 2
# python day15.py filename

import sys

with open(sys.argv[1], 'r') as fi:
    factorA = 16807
    factorB = 48271
    divider = 2147483647
    cycles = 5000000
    remA = int(fi.readline())
    remB = int(fi.readline())
    matches = 0
    for n in range(0, cycles):
        # Perform the computations
        hasValid = False
        while not hasValid:
            remA = (remA * factorA) % divider
            if remA % 4 == 0:
                hasValid = True
        hasValid = False
        while not hasValid:
            remB = (remB * factorB) % divider
            if remB % 8 == 0:
                hasValid = True
        # Mask the remainder against 16 bits and compare
        if remA & 65535 == remB & 65535:
            matches += 1
    print matches
