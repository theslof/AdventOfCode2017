import sys

with open(sys.argv[1], 'r') as fi:
    data = map(int, fi.readline())
    summa = 0
    for i in range(0, len(data)):
        if data[i] == data[i - 1]:
            summa += int(data[i])
    print summa
