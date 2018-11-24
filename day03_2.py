with open('day03.in', 'r') as fi:
    data = int(fi.readline())

array = [[1, 1], [2, 4]]
while True:
    # Rotate the array clockwise
    array = list(zip(*array[::-1]))
    width = len(array[0])
    row = []
    # Build the next row
    for k in range(0, width):
        n = 0
        # If there is a number before k on the same row, add it to the new number
        if len(row) != 0:
            n += row[k - 1]
        # Get a list of the up to three numbers directly above k
        subrow = array[-1][max(k - 1, 0):min(k + 2, width)]
        n += sum(subrow)
        # Add the sum of all neighboring numbers as a new element on the row
        row += [n]
        if n > data:
            print(n)
            exit(0)
    array += [row]
