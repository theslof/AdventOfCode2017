class Registry:
    def __init__(self):
        self.value = 0

    def __int__(self):
        return self.value


regs = dict()
instructions = list()
freq = 0

with open('day18_data', 'r') as fi:
    for row in fi:
        inst = row.split()
        for i in range(1, len(inst)):
            if len(inst[i]) == 1 and ord(inst[i]) >= 97:
                if inst[i] not in regs:
                    regs[inst[i]] = Registry()
                inst[i] = regs[inst[i]]
            else:
                inst[i] = int(inst[i])
        instructions.append(inst)

    pos = 0

    while 0 <= pos < len(instructions):
        inst = instructions[pos]
        if inst[0] == 'snd':
            freq = int(inst[1])
        if inst[0] == 'set':
            inst[1].value = int(inst[2])
        if inst[0] == 'add':
            inst[1].value += int(inst[2])
        if inst[0] == 'mul':
            inst[1].value *= int(inst[2])
        if inst[0] == 'mod':
            inst[1].value %= int(inst[2])
        if inst[0] == 'rcv':
            if int(inst[1]) != 0:
                print(freq)
                exit(0)
        if inst[0] == 'jgz':
            if int(inst[1]) > 0:
                pos += int(inst[2])
                continue
        pos += 1
