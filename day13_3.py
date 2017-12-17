import sys

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
            firewall += [(data[n][1] - 1) * 2]
            n += 1
    # Checking for shortest delay
    delay = 0
    step = 0
    length = len(firewall)
    while step < length:
        f = firewall[step]
        if f != 0 and (delay + step) % f == 0:
            step = -1
            delay += 1
        step += 1
    print delay
