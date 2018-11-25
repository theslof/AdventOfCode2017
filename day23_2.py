from math import sqrt

data = [row.split() for row in open('day23.in', 'r')]
# From my input data:
# Init
# 0 set b 67        b = 67
# 1 set c b         c = b
# 2 jnz a 2         if a == 0:              IGNORED (statement is always FALSE as we init a to 1)
# 3 jnz 1 5             jmp outer_loop      IGNORED
# 4 mul b 100       b *= 100    -> 6700
# 5 sub b -100000   b += 100000 -> 106700
# 6 set c b         c = b       -> 106700
# 7 sub c -17000    c += 17000  -> 123700
#                   for b in range(106700, 123700 + 1, 17) {
#
#    :outer_loop
#    8 set f 1         f = 1   -> 1
#    9 set d 2         d = 2   -> 2    for d in range(2, b) {
#
#       :inner_loop1
#       10 set e 2        e = 2   -> 2    for e in range(2, b) {
#
#          :inner_loop2
#          11 set g d        g = d
#          12 mul g e        g *= e
#          13 sub g b        g -= b  (g = b - d * e)
#          14 jnz g 2        if b == d * e:
#          15 set f 0            f = 0
#
#          :inner_loop3
#          16 sub e -1       e++
#          17 set g e        g = e
#          18 sub g b        g -= b
#          19 jnz g -8       jmp g != 0 inner_loop2   }
#
#       20 sub d -1       d++
#       21 set g d        g = d
#       22 sub g b        g -= b
#       23 jnz g -13      jmp g != 0 inner_loop1  }
#    24 jnz f 2        if f == 0
#    25 sub h -1           h++
#    26 set g b        g = b
#    27 sub g c        g -= c
#    28 jnz g 2        if g == 0 // if b == c
#    29 jnz 1 3            exit
#    30 sub b -17      b += 17
#    31 jnz 1 -23      jmp outer_loop  }


# Translation of assembly to Python3
# Completely garbage runtime, triple loops with insane upper bounds
def unoptimized():
    b = int(data[0][-1])
    b *= int(data[4][-1])
    b -= int(data[5][-1])
    c = b - int(data[7][-1])
    const = -int(data[30][-1])
    h = 0
    for b in range(b, c + 1, const):
        f = 1
        for d in range(2, b):
            for e in range(2, b):
                if b == d * e:
                    f = 0
        if f == 0:
            h += 1
    return h


def optimized():
    b = int(data[0][-1])
    b *= int(data[4][-1])
    b -= int(data[5][-1])
    c = b - int(data[7][-1])
    const = -int(data[30][-1])
    h = 0
    for b in range(b, c + 1, const):
        # The unoptimized code checked if b was equal to any product of two smaller numbers, ie. not a prime.
        # We can improve on this by using a better prime check.
        # First check if it's a multiple of two, then check if it's divisible by any uneven number from 3 to sqrt(b)+1
        if b % 2 == 0 or any(b % d == 0 for d in range(3, int(sqrt(b)) + 1, 2)):
            h += 1
    return h


# print(unoptimized())
print(optimized())
