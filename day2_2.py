with open("day2_data", 'r') as fi:
    checksum = 0
    for line in fi:
        numbers = list(map(int, line.split()))
        for n, first in enumerate(numbers[:-1]):
            for second in numbers[n+1:]:
                large = max(first, second)
                small = min(first, second)
                if large % small == 0:
                    checksum += int(large / small)
print(checksum)
