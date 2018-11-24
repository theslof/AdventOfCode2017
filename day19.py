with open('day19.in', 'r') as fi:
    letters = list()
    grid = list()
    steps = 0
    for row in fi:
        grid.append(row + ' ')
    # We appended a space to every row and append a blank row as the last in the list to avoid index out of range errors
    grid.append(''.join([' ' for _ in range(len(grid[-1]))]))
    x = grid[0].index('|')
    y = 0
    dirx = 0
    diry = 1
    while True:
        if y < 0 or y >= len(grid):
            break
        if x < 0 or x >= len(grid[y]):
            break
        cell = grid[y][x]
        if cell == ' ':
            break
        steps += 1
        if cell == '+':
            if diry != 0:
                if grid[y][x + 1] != '|' and grid[y][x + 1] != ' ':
                    diry = 0
                    dirx = 1
                if grid[y][x - 1] != '|' and grid[y][x - 1] != ' ':
                    diry = 0
                    dirx = -1
            elif dirx != 0:
                if grid[y + 1][x] != '-' and grid[y + 1][x] != ' ':
                    diry = 1
                    dirx = 0
                if grid[y - 1][x] != '-' and grid[y - 1][x] != ' ':
                    diry = -1
                    dirx = 0
        if 64 < ord(cell) < 91:
            # We found a letter, add it!
            letters.append(cell)
        y += diry
        x += dirx
    print(''.join(letters))
    print(steps)
