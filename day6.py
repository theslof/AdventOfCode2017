import sys

states = []

with open(sys.argv[1], 'r') as fi:
    array = map(int, fi.readline().split())
    states += [array[:]]
    unique = True
    numCycles = 0
    while unique:
        largest = max(array)
        n = 0
        for n in range(0, len(array)):
            if largest == array[n]:
                array[n] = 0
                break
        while largest > 0:
            n = (n + 1) % len(array)
            array[n] += 1
            largest -= 1
        numCycles += 1
        for state in states:
            if state == array:
                unique = False
        states += [array[:]]
    print states
    print numCycles
