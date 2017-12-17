import sys

array = [[1, 1], [2, 4]]
a = 4


def numtostr(list):
    string = ''
    for i in list:
        if i < 100:
            string += ' '
        if i < 10:
            string += ' '
        string += str(i) + ' '
    return string


def getcoords(arr, n):
    for y in range(0, len(arr)):
        for x in range(0, len(arr[0])):
            if arr[y][x] == n:
                return y, x
    return None, None


while a < int(sys.argv[1]) + 1:
    array = map(list, zip(*array[::-1]))
    l = len(array[0])
    row = []
    for k in range(0, l):
        n = 0
        if len(row) != 0:
            n += row[k - 1]
        subrow = array[-1][max(k - 1, 0):min(k + 2, l)]
        n += sum(subrow)
        row += [n]
        if n > int(sys.argv[1]):
            print n
            exit(0)
    array += [row]
    a += l
