data = [row.strip().split('/') for row in open('day24.in', 'r')]
tuples = [(int(row[0]), int(row[1])) for row in data]


def longestTupleStrength(tuple_array: [[tuple]]) -> [tuple]:
    longest = []
    strength = 0
    for bridge in tuple_array:
        if len(bridge) > len(longest):
            longest = bridge
        elif len(bridge) == len(longest):
            bs = sum([a+b for a, b in bridge])
            if bs > strength:
                longest = bridge
                strength = bs
    return strength


def findMoreTuples(tuple_array: [tuple], permutations: [[tuple]], seen: set, bridge: [tuple], port: int):
    for tup in tuple_array:
        if tup[0] != port and tup[1] != port or tup in seen:
            continue
        seen.add(tup)
        next_bridge = bridge.copy()
        next_bridge.append(tup)
        permutations.append(next_bridge)
        findMoreTuples(tuple_array, permutations, seen, next_bridge, tup[0] if tup[1] == port else tup[1])
        seen.remove(tup)


all_tuples = []
findMoreTuples(tuples, all_tuples, set(), [], 0)
print(longestTupleStrength(all_tuples))
