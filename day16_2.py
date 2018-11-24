line = [chr(p + 97) for p in range(16)]
permutations = [line]
cycles = 1000000000
with open('day16.in', 'r') as fi:
    moves = [[m[0]] + m[1:].split('/') for m in fi.readline().split(',')]
    count = 0
    newLine = ''
    # Perform the dance until the pattern repeats, which will be the number of unique states.
    while not newLine == line:
        newLine = list(permutations[-1])
        # Uncomment the following line to see all states
#        print(str(count) + ': ' + ''.join(newLine))
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
    print('Pattern repeats after ' + str(count) + ' cycles! The state after ' + str(cycles) + ' cycles is: ')
    print(''.join(permutations[cycles % count]))
