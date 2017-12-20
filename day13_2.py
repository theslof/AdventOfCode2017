import sys


def printarray(array):
    for row in array:
        print row


def step(array):
    for i in range(0, len(array)):
        r, s, x = array[i]
        if s + x < 0 or s + x == r:
            x = -x
        array[i] = (r, s + x, x)


class Packet:
    def __init__(self, delay):
        self.delay = delay
        self.step = 0


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
    delay = 0
    packets = set()
    fw = firewall[:]
    remove = []
    while True:
        packets.add(Packet(delay))
        for p in packets:
            if p.step >= len(firewall):
                print p.delay
                exit(0)
            r, s, x = firewall[p.step]
            if r != 0 and s == 0:
                remove += [p]
                continue
            p.step += 1
        step(firewall)
        delay += 1
        for p in remove:
            packets.remove(p)
        remove = []
