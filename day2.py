import sys

with open(sys.argv[1], 'r') as fi:
    checksum = 0
    for line in fi:
        numbers = map(int, line.split())
        for n in range (0, len(numbers)-1):
            first = numbers[n]
            for m in range (n+1, len(numbers)):
                second = numbers[m]
                if first % second == 0:
                    checksum += first / second
                if second % first == 0:
                    checksum += second / first
print(checksum)
