import collections

weight = {}
children = {}


def totalWeightOf(program):
    # Create a list of weight of children
    cw = [totalWeightOf(c) for c in children[program]]
    if len(set(cw)) < 2:
        # If we have zero elements in set(cw) it's a child-less node, if there's only one all weights are equal.
        # Either way there's no imbalance, so return the total sum of the program.
        return weight[program] + sum(cw)
    # We can only have one child in any given program with a differing weight, so we count how many duplicates we have
    # in our weight list and sort them by most common. The result is split over two tuples, the common weight and the
    # unbalanced weight.
    common, unbalanced = collections.Counter(cw).most_common()
    # We find the index of the program with the unbalanced child,
    i = cw.index(unbalanced[0])
    # then we take the weight of the unbalanced program and add the difference between the common and unbalanced weight
    print(weight[children[program][i]] + common[0] - unbalanced[0])
    # We are now done, no need to backtrack.
    exit(0)


with open('day07.in', 'r') as fi:
    # Setup array
    for line in fi:
        # Program, weight, child programs = Scrub '->' and ',' from the line and split it into words
        p, n, *ps = line.replace('->', '').replace(',', '').split()
        weight[p] = int(n.strip('()'))
        children[p] = ps
    # Create a set of all programs, then remove all programs listed as children. {x for y in z for x in y} = flatten z
    root, = set(children) - {c for child in children.values() for c in child}
    totalWeightOf(root)
