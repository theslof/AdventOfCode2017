with open('day13.in', 'r') as fi:
    # Cleanup of input
    data = [[int(x) for x in row.strip().split(':')] for row in fi]
    # Do the math, iterations is unnecessary
    # [STEPS % (WIDTH * 2 - 2)] is the distance of the scanner from the top slot. If this is zero we have a hit.
    severity = [steps * width for steps, width in data if not steps % (width * 2 - 2)]
    print(sum(severity))
