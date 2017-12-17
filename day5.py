import sys

with open(sys.argv[1], 'r') as fi:
    instr = map(int, fi.readlines())
    jumps = 0
    n = 0
    while len(instr) > n >= 0:
        j = instr[n]
        if j >= 3:
            instr[n] -= 1
        else:
            instr[n] += 1
        n += j
        jumps += 1
print(jumps)
