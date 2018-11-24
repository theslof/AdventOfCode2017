from itertools import count

# Cleanup of input
data = [[int(x) for x in row.strip().split(':')] for row in open('day13.in', 'r')]

print(
    # Fetch the first delay value that results in no collisions
    # Get next DELAY from infinite list of 0-> where DELAY results in no collision for ALL data items
    next(delay for delay in count() if all((steps + delay) % (width * 2 - 2) for steps, width in data)))

# My old loop-based algorithm works fine, but one-liners are cooler
#
#    delay = 0
#    while True:
#        hit = False
#        for steps, width in data:
#            if not (steps + delay) % (width * 2 - 2):
#                delay += 1
#                hit = True
#                break
#        if not hit:
#            break
#    print(delay)
