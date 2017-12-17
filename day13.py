import sys


def printarray(array):
    for row in array:
        print row


with open(sys.argv[1], 'r') as fi:
    data = []
    firewall = []
    for row in fi:
        data += [map(int, row.replace(':', '').split())]
    n = 0
    for i in range(0, data[-1][0] + 1):
        if data[n][0] > i:
            firewall += [(0, 0, 0)]
        else:
            firewall += [(data[n][1], 0, 1)]
            n += 1
    severity = 0
    for n in range(0, len(firewall)):
        r, s, x = firewall[n]
        if s == 0:
            severity += n * r
        for i in range(0, len(firewall)):
            r, s, x = firewall[i]
            if s + x < 0 or s + x == r:
                x = -x
            firewall[i] = (r, s + x, x)
    print severity
