from math import sqrt
rules = [(p, op) for p, op in (row.replace('=>', '').split() for row in open("day21.in", 'r'))]


# Print 2D array of strings without decorations
def prettyPrint(array: [[str]]) -> None:
    for row in array:
        print(' '.join([x for y in row for x in y]))
    print()


# Rotate a 2D array 90 degrees clockwise
def rotate(block: [[str]]) -> [[str]]:
    return [''.join(row) for row in list(zip(*block[::-1]))]


# Enhance a 2D string array according to ruleset
def enhance(block: [[str]]) -> [[str]]:
    for _ in range(2):
        for _ in range(4):
            block = rotate(block)
            row_string = '/'.join(block)
            for (ruleList, newPattern) in rules:
                if row_string == ruleList:
                    return newPattern.split('/')
        block = block[::-1]


# Split a 2D array into multiple arrays of specified size
def splitArray(array: [[str]], size: int) -> [[[str]]]:
    if len(array) < 4:
        return [array]
    return [subSlice(array, y, x, size) for y in range(0, len(array), size) for x in range(0, len(array), size)]


# Get the sub-array of specified size starting at specified coordinates
def subSlice(array: [[str]], y: int, x: int, size: int) -> [[str]]:
    return [row[x: x+size] for row in array[y: y+size]]


# Join array of sub-arrays of specified width into one big array
def joinBlocks(array: [[[str]]], width: int) -> [[str]]:
    if len(array) < 4:
        return array
    root = int(sqrt(len(array)))
    ret = []
    for y in range(0, len(array), root):
        for x in range(width):
            sub_data = []
            for o in range(root):
                sub_data.append(array[y + o][x])
            ret.append(''.join(sub_data))
    return ret


def main(array: [str], iterations: int, should_print: bool) -> int:
    # Do initial enhance, we don't need to split/merge
    array = enhance(array)
    for _ in range(iterations - 1):
        width = 3
        # If the array width is not evenly divisible by two it's evenly divisible by three
        if len(array) % 2:
            width = 4
        # Split array and enhance each sub-array according to rules, then merge back into one array
        array = joinBlocks([enhance(block) for block in splitArray(array, width - 1)], width)
    if should_print:
        prettyPrint(array)
    # Count the amount of #-characters in array
    return len([x for row in array for x in row if x == '#'])


data = ['.#.', '..#', '###']
print('Part 1: ' + str(main(data, 5, True)))
print('Part 2: ' + str(main(data, 18, False)))
