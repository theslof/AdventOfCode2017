step = int(open('day17.in', 'r').readline())
spinlock = [0, 1]
index = 1
cycles = 2017
for i in range(2, cycles + 1):
    index = (index + step) % i + 1
    spinlock = spinlock[0:index] + [i] + spinlock[index:]
print(spinlock[index + 1])
