import sys

with open(sys.argv[1], 'r') as fi:
    spinlock = [0,1]
    index = 1
    cycles = 2017
    step = int(fi.readline())
    for i in range(2, cycles + 1):
        index = (index + step) % len(spinlock) + 1
        spinlock = spinlock[0:index] + [i] + spinlock[index:]
    print spinlock[index + 1]
