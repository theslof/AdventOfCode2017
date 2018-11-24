with open('day15.in', 'r') as fi:
    remA = int(fi.readline().split()[-1])
    remB = int(fi.readline().split()[-1])
    factorA = 16807
    factorB = 48271
    divider = 2147483647
    cycles = 40000000
    matches = 0
    for n in range(cycles):
        # Perform the computations
        remA = (remA * factorA) % divider
        remB = (remB * factorB) % divider
        # Mask the remainder against 16 bits and compare
        if remA & 0xFFFF == remB & 0xFFFF:
            matches += 1
    print(matches)
