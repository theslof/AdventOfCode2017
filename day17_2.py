# Important note is that 0 is always the first element in the spinlock list.
# Therefore we don't actually have to keep track of any list, we only have
# to do our computations and save the current value whenever the index lands
# on the second element.
# I'm hungry, so I may be missing some major loop-free optimization.

import sys

with open(sys.argv[1], 'r') as fi:
    index = 1
    cycles = 50000000
    step = int(fi.readline())
    solution = 1
    for i in range(2, cycles + 1):
        index = (index + step) % i + 1
        if index - 1 == 0:
            solution = i
    print solution
