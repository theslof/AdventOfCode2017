class Program:
    def __init__(self):
        self.group = {self}


with open('day12_data', 'r') as fi:
    groups = list()
    programs = list()
    connections = list()
    current = 0
    # Setup: Parse file and setup all Program objects
    for row in fi:
        data = list(map(int, row.replace(',', '').replace('<-> ', '').split()))
        programs.append(Program())
        connections.append(data[1:])
    # Connect all Programs with a connection by merging their groups
    for i in range(len(connections)):
        for n in connections[i]:
            if programs[i].group != programs[n].group:
                # The programs share a connection but are in separate groups
                for p in programs[n].group:
                    # Add all the programs from n's group to i's group
                    programs[i].group.add(p)
                    p.group = programs[i].group
    # Build a list of unique groups
    for p in programs:
        if p.group not in groups:
            groups.append(p.group)

    print(len(groups))
