REGISTER_SIZE = 10000


class State:
    def __init__(self, zero_num: int, zero_dir: int, zero_state: str, one_num: int, one_dir: int, one_state: str):
        self.zero_num = zero_num
        self.zero_dir = zero_dir
        self.zero_state = zero_state
        self.one_num = one_num
        self.one_dir = one_dir
        self.one_state = one_state


states = dict()
registers = [0 for _ in range(REGISTER_SIZE)]
pos = int(REGISTER_SIZE / 2)

with open("day25.in", 'r') as fi:
    state = fi.readline().strip('.').split()[-1][0]
    steps = int(fi.readline().split()[-2])
    while True:
        line = fi.readline()
        if not line:
            break
        sstate = fi.readline(10)[-1]
        fi.readline()
        fi.readline()
        zval = int(fi.readline().split()[-1][0])
        zdir = 1 if fi.readline().split()[-1] == 'right.' else -1
        zstate = fi.readline().split()[-1][0]
        fi.readline()
        oval = int(fi.readline().split()[-1][0])
        odir = 1 if fi.readline().split()[-1] == 'right.' else -1
        ostate = fi.readline().split()[-1][0]
        states[sstate] = State(zval, zdir, zstate, oval, odir, ostate)

for _ in range(steps):
    curVal = registers[pos]
    if curVal == 0:
        registers[pos] = states[state].zero_num
        pos += states[state].zero_dir
        state = states[state].zero_state
    else:
        registers[pos] = states[state].one_num
        pos += states[state].one_dir
        state = states[state].one_state

print(sum(registers))
