#  - Decide which way to turn based on the current node:
#      - If it is clean, it turns left.
#      - If it is weakened, it does not turn, and will continue moving in the same direction.
#      - If it is infected, it turns right.
#      - If it is flagged, it reverses direction, and will go back the way it came.
#  - Modify the state of the current node, as described above.
#  - The virus carrier moves forward one node in the direction it is facing.

in_data = [[cell == '#' for cell in row if cell in '.#'] for row in open('day22.in', 'r')]
iterations = 10000000
verbose = False


def prettyPrint(array: [[int]], cy = -1, cx = -1):
    for y, row in enumerate(array):
        srow = []
        for x, cell in enumerate(row):
            if cell == 0:  # Clean
                srow.append('O' if x == cx and y == cy else '.')
            elif cell == 1:  # Weak
                srow.append('W' if x == cx and y == cy else 'w')
            elif cell == 2:  # Infected
                srow.append('X' if x == cx and y == cy else '#')
            elif cell == 3:  # Flagged
                srow.append('F' if x == cx and y == cy else 'f')
            srow.append(' ')
        print(''.join(srow))


def trim(array: [[int]]):
    num_blank_start = 0
    num_blank_end = len(array)
    first_index = len(array)
    last_index = 0
    # Find all blank rows at start
    for row in array:
        if not any([x == 1 or x == 2 or x == 3 for x in row]):
            num_blank_start += 1
        else:
            break
    # Find all blank rows at end
    for row in array[::-1]:
        if not any([x == 1 or x == 2 or x == 3 for x in row]):
            num_blank_end -= 1
        else:
            break
    # Find first/last True index on a row
    for row in array[num_blank_start: num_blank_end]:
        first_index = min(first_index, fIndex(row, 1), fIndex(row, 2), fIndex(row, 3))
        last_index = max(last_index, rIndex(row, 1), rIndex(row, 2), rIndex(row, 3))
    return [row[first_index:last_index] for row in array[num_blank_start: num_blank_end]]


def fIndex(mlist: list, obj: object):
    for i, o in enumerate(mlist):
        if o == obj:
            return i
    return len(mlist)


def rIndex(mlist: list, obj: object):
    for i, o in enumerate(mlist[::-1]):
        if o == obj:
            return len(mlist) - i
    return -1


def writeToFile(array: [[int]], file_name: str):
    fi = open(file_name, 'w')
    for y, row in enumerate(array):
        srow = []
        for x, cell in enumerate(row):
            if cell == 0:  # Clean
                srow.append('.')
            elif cell == 1:  # Weak
                srow.append('W')
            elif cell == 2:  # Infected
                srow.append('#')
            elif cell == 3:  # Flagged
                srow.append('F')
            srow.append(' ')
        fi.write(''.join(srow) + '\n')


def printv(string: str):
    if verbose:
        print(string)


start_size = 1000
virus_map = [[0 for _ in range(start_size)] for _ in range(start_size)]

for y, row in enumerate(in_data):
    for x, v in enumerate(row):
        virus_map[int(start_size / 2 - len(in_data) / 2 + y)][int(start_size / 2 - len(row) / 2 + x)] = 2 if v else 0

xspeed = 0
yspeed = -1
xpos = int(start_size / 2 - 1)
ypos = int(start_size / 2 - 1)

counter = 0

for _ in range(iterations):
    infection_type = virus_map[ypos][xpos]
    if infection_type == 0:
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
        virus_map[ypos][xpos] = 1
    elif infection_type == 1:
        printv('weak, keep going')
        virus_map[ypos][xpos] = 2
        counter += 1
    elif infection_type == 2:
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
        virus_map[ypos][xpos] = 3
    else:
        printv('flagged, reverse')
        xspeed = -xspeed
        yspeed = -yspeed
        virus_map[ypos][xpos] = 0
    ypos += yspeed
    xpos += xspeed
#prettyPrint(trim(virus_map), xpos, ypos)
#writeToFile(trim(virus_map), 'day22.out')
print(counter)
