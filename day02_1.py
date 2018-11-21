with open("day02_data", 'r') as fi:
    # Dirty list comprehension, read bottom up:
    print(
        # sum results
        sum(
            # subtract the smallest int in list from largest
            [(max(row) - min(row)) for row in [list(
                # split each row into a list of ints
                map(int, row.split()))
                # for all rows in file
                for row in fi]]))
