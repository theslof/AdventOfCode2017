import sys

with open(sys.argv[1], 'r') as fi:
    f = fi.readline()
    print(f)
    halfway = len(f) / 2
    index = 0
    sumOfNums = 0
    while index < len(f):
        if f[index] == f[index - halfway]:
            sumOfNums += int(f[index])
        index += 1
print(sumOfNums)
