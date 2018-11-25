# - If the current node is infected, it turns to its right. Otherwise, it turns to its left.
#    (Turning is done in-place; the current node does not change.)
# - If the current node is clean, it becomes infected. Otherwise, it becomes cleaned.
#    (This is done after the node is considered for the purposes of changing direction.)
# - The virus carrier moves forward one node in the direction it is facing.
in_data = [[cell == '#' for cell in row if cell in '.#'] for row in open('day22.in', 'r')]
iterations = 10000
verbose = False


def prettyPrint(array: [[bool]], cy = -1, cx = -1):
    for y, row in enumerate(array):
        srow = []
        for x, cell in enumerate(row):
            if x == cx and y == cy:
                srow.append('X' if cell else 'o')
            else:
                srow.append('#' if cell else '.')
            srow.append(' ')
        print(''.join(srow))


def trim(array: [[bool]]):
    num_blank_start = 0
    num_blank_end = len(array)
    first_index = len(array)
    last_index = 0
    # Find all blank rows at start
    for row in array:
        if not any(row):
            num_blank_start += 1
        else:
            break
    # Find all blank rows at end
    for row in array[::-1]:
        if not any(row):
            num_blank_end -= 1
        else:
            break
    # Find first/last True index on a row
    for row in array[num_blank_start: num_blank_end]:
        first_index = min(first_index, row.index(True))
        last_index = max(last_index, len(row) - row[::-1].index(True))
    return [row[first_index:last_index] for row in array[num_blank_start: num_blank_end]]


def writeToFile(array: [[bool]], file_name: str):
    fi = open(file_name, 'w')
    for y, row in enumerate(array):
        srow = []
        for x, cell in enumerate(row):
            srow.append('#' if cell else '.')
            srow.append(' ')
        fi.write(''.join(srow) + '\n')


def printv(string: str):
    if verbose:
        print(string)


start_size = 1000
virus_map = [[False for _ in range(start_size)] for _ in range(start_size)]

for y, row in enumerate(in_data):
    for x, v in enumerate(row):
        virus_map[int(start_size / 2 - len(in_data) / 2 + y)][int(start_size / 2 - len(row) / 2 + x)] = v

xspeed = 0
yspeed = -1
xpos = int(start_size / 2 - 1)
ypos = int(start_size / 2 - 1)

counter = 0

for _ in range(iterations):
    is_infected = virus_map[ypos][xpos]
    if is_infected:
        printv('infected, turn right')
        if yspeed < 0:
            yspeed = 0
            xspeed = 1
            printv('new dir: >')
        elif xspeed > 0:
            yspeed = 1
            xspeed = 0
            printv('new dir: v')
        elif yspeed > 0:
            yspeed = 0
            xspeed = -1
            printv('new dir: <')
        else:
            yspeed = -1
            xspeed = 0
            printv('new dir: ^')
    else:
        counter += 1
        printv('not infected, turn left')
        if yspeed < 0:
            yspeed = 0
            xspeed = -1
            printv('new dir: <')
        elif xspeed > 0:
            yspeed = -1
            xspeed = 0
            printv('new dir: ^')
        elif yspeed > 0:
            yspeed = 0
            xspeed = 1
            printv('new dir: >')
        else:
            yspeed = 1
            xspeed = 0
            printv('new dir: v')
    virus_map[ypos][xpos] = not is_infected
    ypos += yspeed
    xpos += xspeed
#prettyPrint(virus_map, xpos, ypos)
writeToFile(trim(virus_map), 'day22.out')
print(counter)
