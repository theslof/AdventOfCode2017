with open("day01.in", 'r') as fi:
    data = list(map(int, fi.readline()))
    sum = 0
    for index, digit in enumerate(data):
        if digit == data[index - 1]:
            sum += digit
    print(sum)
