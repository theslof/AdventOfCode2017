def isvalid(line):
    words = line.split()
    words = list(map(''.join, map(sorted, words)))

    for i, n in enumerate(words[:-1]):
        for j in words[i+1:]:
            if words[i] == j:
                return False
    return True


with open('day04.in', 'r') as fi:
    sumOfValid = 0
    for line in fi:
        if isvalid(line):
            sumOfValid += 1
    print(sumOfValid)
