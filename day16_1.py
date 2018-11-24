line = [chr(p + 97) for p in range(16)]
with open('day16.in', 'r') as fi:
    moves = [[m[0]] + m[1:].split('/') for m in fi.readline().split(',')]
    for move in moves:
        if move[0] == 's':
            # Spin
            n = int(move[1])
            line = line[-n:] + line[0:-n]
        elif move[0] == 'x':
            # Exchange programs by index
            a = int(move[1])
            b = int(move[2])
            pa = line[a]
            pb = line[b]
            line[b] = pa
            line[a] = pb
        elif move[0] == 'p':
            # Exchange programs by name
            a = line.index(move[1])
            b = line.index(move[2])
            pa = line[a]
            pb = line[b]
            line[b] = pa
            line[a] = pb
    print(''.join(line))
