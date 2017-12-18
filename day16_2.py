import sys

line = [chr(p + 97) for p in range(0, 16)]
permutations = [line]
cycles = 1000000000
with open(sys.argv[1], 'r') as fi:
    moves = [[m[0]] + m[1:].split('/') for m in fi.readline().split(',')]
    count = 0
    print '0: ' + ''.join(line)
    match = False
    # Perform the dance until the pattern repeats, which will be the number of unique states.
    while not match:
        newLine = list(permutations[-1])
        print str(count) + ': ' + ''.join(newLine)
        count += 1
        # Dance
        for move in moves:
            if move[0] == 's':
                # Spin
                n = int(move[1])
                newLine = newLine[-n:] + newLine[0:-n]
            if move[0] == 'x':
                # Exchange programs by index
                a = int(move[1])
                b = int(move[2])
                pa = newLine[a]
                pb = newLine[b]
                newLine[b] = pa
                newLine[a] = pb
            if move[0] == 'p':
                # Exchange programs by name
                a = newLine.index(move[1])
                b = newLine.index(move[2])
                pa = newLine[a]
                pb = newLine[b]
                newLine[b] = pa
                newLine[a] = pb
        permutations.append(newLine)
        match = newLine == line
    print 'Pattern repeats after ' + str(count) + ' cycles! The state after all cycles is: '
    print str(cycles % count) + ': ' + ''.join(permutations[cycles % count])
