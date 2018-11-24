with open("day01.in", 'r') as fi:
    data = list(map(int, fi.readline()))
    halfway = int(len(data) / 2)
    index = 0
    sum = 0
    for index, digit in enumerate(data):
        if digit == data[index - halfway]:
            sum += digit
    print(sum)
