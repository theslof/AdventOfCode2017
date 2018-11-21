with open('day06_data', 'r') as fi:
    states = []
    array = [int(x) for x in fi.readline().split()]
    numCycles = 0
    while array not in states:
        states.append(array[:])
        largest = max(array)
        n = array.index(largest)
        array[n] = 0
        while largest:
            n = (n + 1) % len(array)
            array[n] += 1
            largest -= 1
        numCycles += 1
    print(len(states) - states.index(array))
