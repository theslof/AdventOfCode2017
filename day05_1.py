with open('day05.in', 'r') as fi:
    instr: [int] = [int(x) for x in fi]
    length: int = len(instr)
    jumps: int = 0
    n: int = 0
    while 0 <= n < length:
        j = instr[n]
        instr[n] += 1
        n += j
        jumps += 1
print(jumps)
