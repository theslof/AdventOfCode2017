import sys


def printarray(array):
    for row in array:
        print row


with open(sys.argv[1], 'r') as fi:
    letters = list()
    grid = list()
    steps = 0
    for row in fi:
        grid.append(row)
    x = grid[0].index('|')
    y = 0
    dirx = 0
    diry = 1
    while True:
        if y < 0 or y >= len(grid):
            break
        if x < 0 or x >= len(grid[y]):
            break
        if grid[y][x] == ' ':
            break
        steps += 1
        if grid[y][x] == '+':
            if diry != 0:
                if grid[y][x + 1] != '|' and grid[y][x + 1] != ' ':
                    diry = 0
                    dirx = 1
                if grid[y][x - 1] != '|' and grid[y][x - 1] != ' ':
                    diry = 0
                    dirx = -1
            else:
                if dirx != 0:
                    if grid[y + 1][x] != '-' and grid[y + 1][x] != ' ':
                        diry = 1
                        dirx = 0
                    if grid[y - 1][x] != '-' and grid[y - 1][x] != ' ':
                        diry = -1
                        dirx = 0
        if 64 < ord(grid[y][x]) < 91:
            letters.append(grid[y][x])
        y += diry
        x += dirx
    print ''.join(letters)
    print steps
