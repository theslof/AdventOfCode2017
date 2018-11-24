with open('day15.in', 'r') as fi:
    remA = int(fi.readline().split()[-1])
    remB = int(fi.readline().split()[-1])
    factorA = 16807
    factorB = 48271
    divider = 2147483647
    cycles = 5000000
    matches = 0
    for n in range(cycles):
        # Perform the computations
        while True:
            remA = (remA * factorA) % divider
            if not remA & 3:
                break
        while True:
            remB = (remB * factorB) % divider
            if not remB & 7:
                break
        # Mask the remainder against 16 bits and compare
        if remA & 0xFFFF == remB & 0xFFFF:
            matches += 1
    print(matches)
