import re


def manhattan(steps, p, v, a):
    cx = p[0] + steps * (v[0] + steps * a[0])
    cy = p[1] + steps * (v[1] + steps * a[1])
    cz = p[2] + steps * (v[2] + steps * a[2])
    return int(abs(cx) + abs(cy) + abs(cz))


with open('day20.in', 'r') as fi:
    data = list()
    i = 0
    for row in fi:
        p, v, a, *_ = re.findall('<(.*?)>', row)
        pl = list(map(int, p.split(',')))
        vl = list(map(int, v.split(',')))
        al = list(map(int, a.split(',')))
        data.append((i, manhattan(1000, pl, vl, al)))
        i += 1

    dist = [(d, i) for i, d in data]
    print(min(dist)[1])
