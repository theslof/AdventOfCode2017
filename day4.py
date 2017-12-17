import sys


def isvalid(line):
    words = line.split()
    words = map(''.join, map(sorted, words))

    for i in range(0, len(words) - 1):
        for j in range(i + 1, len(words)):
            if words[i] == words[j]:
                return False
    return True


with open(sys.argv[1], 'r') as fi:
    sumOfValid = 0
    valids = map(isvalid, fi.readlines())
    for v in valids:
        if v:
            sumOfValid += 1
    print sumOfValid
