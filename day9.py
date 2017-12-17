import sys


def printarray(array):
    for row in array:
        print row


def scrub(s):
    i = 0
    garbagenum = 0
    while i < len(s):
        if s[i] == '!':
            s = s[0:i] + s[i + 2:]
        else:
            i += 1
    i = 0
    a = -1
    while i < len(s):
        if s[i] == '<' and a < 0:
            a = i
            i += 1
        if s[i] == '>' and a >= 0:
            garbagenum += (i - a - 1)
            s = s[0:a] + s[i + 1:]
            i = a
            a = -1
        else:
            i += 1
    s = s.replace('{', '[').replace('}', ']').replace(',]', ']').replace('[,', '[')
    print garbagenum
    return s


def count(array, depth):
    if len(array) == 0:
        return depth
    return sum([count(next, depth + 1) for next in array]) + depth


with open(sys.argv[1], 'r') as fi:
    data = scrub(fi.read())
    array = eval(data)
#    print array
    print count(array, 1)
