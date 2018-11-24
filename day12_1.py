def visit(programs, visited, current):
    visited.append(current)
    return 1 + sum([visit(programs, visited + programs[current], v) for v in programs[current] if v not in visited])


with open('day12.in', 'r') as fi:
    pipes = {}
    for row in fi:
        data = list(row.replace(',', '').split())
        pipes[data[0]] = data[2:]
    print(visit(pipes, [], '0'))
