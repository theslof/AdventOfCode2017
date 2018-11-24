# Important note is that 0 is always the first element in the spinlock list.
# Therefore we don't actually have to keep track of any list, we only have
# to do our computations and save the current value whenever the index lands
# on the second element.

index = 1
cycles = 50000000
step = int(open('day17_data', 'r').readline())
solution = 1
for i in range(2, cycles + 1):
    index = (index + step) % i + 1
    if index == 1:
        solution = i
print(solution)
