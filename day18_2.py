class Registry:
    def __init__(self, n):
        self.value = n

    def __int__(self):
        return self.value


class Thread:
    def __init__(self, p):
        self.freq = list()
        self.twin = None
        self.pos = 0
        self.running = True
        self.waiting = False
        self.regs = dict()
        self.regs['p'] = Registry(p)
        self.regs['a'] = Registry(0)
        self.regs['b'] = Registry(0)
        self.regs['f'] = Registry(0)
        self.regs['1'] = Registry(0)
        self.instructions = list()
        self.sent = 0

    def step(self):
        if not self.running:
            return
        if 0 > self.pos or self.pos >= len(self.instructions):
            self.running = False
            self.waiting = True
            return
        inst = self.instructions[self.pos]
        if inst[0] == 'snd':
            self.twin.freq.append(int(inst[1]))
            self.sent += 1
        if inst[0] == 'set':
            inst[1].value = int(inst[2])
        if inst[0] == 'add':
            inst[1].value += int(inst[2])
        if inst[0] == 'mul':
            inst[1].value *= int(inst[2])
        if inst[0] == 'mod':
            inst[1].value %= int(inst[2])
        if inst[0] == 'rcv':
            if len(self.freq) == 0:
                self.waiting = True
                return
            else:
                self.waiting = False
                inst[1].value = self.freq[0]
                self.freq = self.freq[1:]
        if inst[0] == 'jgz':
            if int(inst[1]) > 0:
                self.pos += int(inst[2])
                return
        self.pos += 1
        return


instructions = list()
freq = 0
thread0 = Thread(0)
thread1 = Thread(1)
thread0.twin = thread1
thread1.twin = thread0

with open('day18.in', 'r') as fi:
    for row in fi:
        inst = row.split()
        inst0 = inst[:]
        inst1 = inst[:]
        for i in range(1, len(inst)):
            if len(inst[i]) == 1 and ord(inst[i]) >= 97:
                if inst[i] not in thread0.regs:
                    thread0.regs[inst[i]] = Registry(0)
                    thread1.regs[inst[i]] = Registry(0)
                inst0[i] = thread0.regs[inst[i]]
                inst1[i] = thread1.regs[inst[i]]
            else:
                inst0[i] = int(inst[i])
                inst1[i] = int(inst[i])
        thread0.instructions.append(inst0)
        thread1.instructions.append(inst1)

    while not (thread1.waiting and thread0.waiting):
        thread0.step()
        thread1.step()
    print(thread1.sent)
