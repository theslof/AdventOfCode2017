import sys


def printarray(array):
    for row in array:
        print row


def checkEqual1(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)


def buildtower(program, array):
    for row in array:
        if program != row[0]:
            continue
        return [row[0], int(row[1].strip('()'))] + [buildtower(p, array) for p in row[3:]]


def sumweights(array):
    if len(array) == 0:
        return 0
    if len(array[2:]) == 0:
        return array[1]
    ws = array[1]
    warray = []
    for row in array[2:]:
        warray += [sumweights(row)]
    if not checkEqual1(warray):
        print [[name[0], name[1]] for name in array[2:]]
        print warray
    ws += sum(warray)
    return ws


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
    struct = buildtower(root, programs)
    sumweights(struct)
