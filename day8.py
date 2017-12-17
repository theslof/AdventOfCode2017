import sys


def printarray(array):
    for row in array:
        print row


instructions = []
regs = {}
largest = 0

with open(sys.argv[1], 'r') as fi:
    for row in fi:
        instructions += [row.split()]
    for row in instructions:
        a = regs.get(row[0], 0)
        b = str(regs.get(row[4], 0))
        if eval(b+row[5]+row[6]):
            if row[1] == 'inc':
                a += int(row[2])
            if row[1] == 'dec':
                a -= int(row[2])
            regs[row[0]] = a
            if a > largest:
                largest = a
    printarray(instructions)
    print (regs)
    print 'current max: ' + str(max(regs.values()))
    print 'all-time max: ' + str(largest)
