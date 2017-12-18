import sys


class Program:
    def __init__(self, n):
        self.name = n


line = [chr(p + 97) for p in range(0, 16)]
with open(sys.argv[1], 'r') as fi:
    moves = [[m[0]] + m[1:].split('/') for m in fi.readline().split(',')]
    print line
    for move in moves:
        if move[0] == 's':
            # Spin
            n = int(move[1])
            line = line[-n:] + line[0:-n]
        if move[0] == 'x':
            # Exchange programs by index
            a = int(move[1])
            b = int(move[2])
            pa = line[a]
            pb = line[b]
            line[b] = pa
            line[a] = pb
        if move[0] == 'p':
            # Exchange programs by name
            a = line.index(move[1])
            b = line.index(move[2])
            pa = line[a]
            pb = line[b]
            line[b] = pa
            line[a] = pb
    print ''.join(line)
