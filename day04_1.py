with open('day04.in', 'r') as fi:
    lines = 0
    for line in fi:
        words = line.split()
        if len(words) == len(set(words)):
            lines += 1
    print(lines)
