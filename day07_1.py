with open('day07_data', 'r') as fi:
    weight = {}
    children = {}

    # Setup array
    for line in fi:
        # Program, weight, child programs = Scrub '->' and ',' from the line and split it into words
        p, n, *ps = line.replace('->', '').replace(',', '').split()
        weight[p] = int(n.strip('()'))
        children[p] = ps
    # Create a set of all programs, then remove all programs listed as children. {x for y in z for x in y} = flatten z
    root, = set(children) - {c for child in children.values() for c in child}
    print(root)
