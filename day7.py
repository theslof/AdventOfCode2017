import sys


def printarray(array):
    for row in array:
        print row


programs = []

with open(sys.argv[1], 'r') as fi:
    for line in fi:
        programs += [[s.strip(',') for s in line.split()]]
    root = programs[0][0]
    for i in range(0, len(programs) - 1):
        for j in range(i + 1, len(programs)):
            for program in programs[j][3:]:
                if root == program:
                    root = programs[j][0]
    print 'root = ' + root
