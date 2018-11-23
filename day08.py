regs = {}
largest = 0

with open('day08_data', 'r') as fi:
    instructions = [row.replace('if', '').replace('inc', '+').replace('dec', '-').split() for row in fi]
    for reg1, op, reg2, reg3, cond, val in instructions:
        a = regs.get(reg1, 0)
        b = regs.get(reg3, 0)
        if eval(str(b)+cond+val):
            a = eval(str(a)+op+reg2)
            regs[reg1] = a
            largest = max(a, largest)
    print('current max: ' + str(max(regs.values())))
    print('all-time max: ' + str(largest))
