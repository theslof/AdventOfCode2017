data = 347991

root = 0
square = 0
for x in range(1, data, 2):
    if x*x >= data:
        root = x
        square = x*x
        break

diff = square - data
root2 = int(root / 2)
offset = abs(root2 - (diff % (root-1)))
manhattan = root2 + offset
print(manhattan)
