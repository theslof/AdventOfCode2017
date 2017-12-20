import sys

with open(sys.argv[1], 'r') as fi:
    print sum([max(row) - min(row) for row in (map(int, row.split()) for row in fi)])
