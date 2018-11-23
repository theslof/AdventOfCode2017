import re


def count(array, depth):
    if len(array):
        return sum([count(subarray, depth + 1) for subarray in array]) + depth
    return depth


with open('day09_data', 'r') as fi:
    s = fi.readline()
    # Scrub all '!.'
    s = re.sub('!.', '', s)
    # Scrub all substrings between < and >
    s = re.sub('<(.*?)>', '', s)
    # Cleanup for counting
    s = s.replace('{', '[').replace('}', ']').replace(',]', ']').replace('[,', '[')
    print(count(eval(s), 1))
