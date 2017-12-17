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
            firewall += [0]
        else:
            firewall += [(data[n][1]-1) * 2]
            n += 1
    delay = 0
    match = False
    while not match:
        match = True
        for step in range(0, len(firewall)):
            print (delay, step, firewall[step])
            if firewall[step] != 0 and (delay + step) % firewall[step] == 0:
                match = False
                delay += 1
                break
    print delay
    delay = 0
    step = 0
    length = len(firewall)
    while step < length:
        print (delay, step, firewall[step])
        if firewall[step] != 0 and (delay + step) % firewall[step] == 0:
            step = 0
            delay += 1
        step += 1
    print length, step
    print delay

