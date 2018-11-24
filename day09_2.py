import re


with open('day09.in', 'r') as fi:
    # Scrub all '!.'
    s = re.sub('!.', '', fi.read())
    # Find all substrings between < and >, flatten array and count the characters
    print(len([a for b in re.findall('<(.*?)>', s) for a in b]))
