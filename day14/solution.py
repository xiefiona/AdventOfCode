from collections import defaultdict

# part 1
def get_weight(rockInd, numRocks):
    tot = 0
    for _ in range(numRocks):
        tot += rockInd
        rockInd -= 1
    return tot

def parse(graph):
    weight = 0
    graph = ['#'*len(graph[0])] + graph
    for col in range(len(graph[0])):
        numRocks = 0
        for i, row in enumerate(reversed(range(len(graph)))):
            if graph[row][col] == 'O':
                numRocks += 1
            elif graph[row][col] == '#':
                weight += get_weight(i, numRocks)
                numRocks = 0
    return weight

# part 2
def get_vert_rocks(rocksSet):
    circleRocksVert = defaultdict(set)
    for (r,c) in rocksSet:
        circleRocksVert[c].add(r)
    return circleRocksVert

def get_hoz_rocks(rocksSet):
    circleRocksHoz = defaultdict(set)
    for (r,c) in rocksSet:
        circleRocksHoz[r].add(c)
    return circleRocksHoz

def calculate_score(rocks, maxnum):
    return sum([maxnum - r for r,_ in rocks])

def get_rocks(rocksDict, orientation):
    rocks = set()
    for row, colRocks in rocksDict.items():
            for col in colRocks:
                rocks.add((row, col))
    if orientation == 'vert':
        rocks = set((r,c) for (c,r) in rocks)
    return rocks

memo = {}

def shift_rocks(graph):
    sqRocks = [(r,c) for r in range(len(graph)) for c in range(len(graph[0])) if graph[r][c] == '#'] + [(-1,c) for c in range(len(graph[0]))] + [(len(graph), c) for c in range(len(graph[0]))]
    sqRocks += [(r,-1) for r in range(len(graph))] + [(r,len(graph[0])) for r in range(len(graph))]
    sqRocksHoz = defaultdict(list)
    sqRocksVert = defaultdict(list)
    for (r,c) in sqRocks:
        sqRocksHoz[r].append(c)
        sqRocksVert[c].append(r)
    [vals.sort() for vals in sqRocksHoz.values()]
    [vals.sort() for vals in sqRocksVert.values()]

    circleRocks = set([(r,c) for r in range(len(graph)) for c in range(len(graph[0])) if graph[r][c] == 'O'])

    seq = [circleRocks]
    for i in range(1000000000):

        # shift north
        circleRocksVert = get_vert_rocks(circleRocks)
        for scol, srows in sorted(sqRocksVert.items()):
            prevrow = 0
            for row in srows:
                if scol in circleRocksVert:
                    movingRocks = [x for x in circleRocksVert[scol] if prevrow < x < row]
                    # change their positions
                    [circleRocksVert[scol].remove(rock) for i, rock in enumerate(movingRocks)]
                    [circleRocksVert[scol].add(prevrow+i+1) for i, rock in enumerate(movingRocks)]
                prevrow = row
        circleRocks = get_rocks(circleRocksVert, 'vert')

        # shift west
        circleRocksHoz = get_hoz_rocks(circleRocks)
        for srow, scols in sorted(sqRocksHoz.items()):
            # scols.sort()
            prevrow = 0
            for row in scols:
                if srow in circleRocksHoz:
                    movingRocks = [x for x in circleRocksHoz[srow] if prevrow < x < row]
                    [circleRocksHoz[srow].remove(rock) for i, rock in enumerate(movingRocks)]
                    [circleRocksHoz[srow].add(prevrow+i+1) for i, rock in enumerate(movingRocks)]
                prevrow = row
        circleRocks = get_rocks(circleRocksHoz, 'hoz')

        # shift south
        circleRocksVert = get_vert_rocks(circleRocks)
        for scol, srows in sorted(sqRocksVert.items()):
            prevrow = 0
            for row in srows:
                if scol in circleRocksVert:
                    movingRocks = [x for x in circleRocksVert[scol] if prevrow < x < row]
                    [circleRocksVert[scol].remove(rock) for i, rock in enumerate(movingRocks)]
                    [circleRocksVert[scol].add(row-i-1) for i, rock in enumerate(movingRocks)] 
                prevrow = row
        circleRocks = get_rocks(circleRocksVert, 'vert')

        # shift east
        circleRocksHoz = get_hoz_rocks(circleRocks)
        for srow, scols in sorted(sqRocksHoz.items()):
            prevrow = 0
            for row in scols:
                if srow in circleRocksHoz:
                    movingRocks = [x for x in circleRocksHoz[srow] if prevrow < x < row]
                    [circleRocksHoz[srow].remove(rock) for i, rock in enumerate(movingRocks)]
                    [circleRocksHoz[srow].add(row-i-1) for i, rock in enumerate(movingRocks)] 
                prevrow = row
        circleRocks = get_rocks(circleRocksHoz, 'hoz')
        
        if circleRocks in seq:
            seq.append(circleRocks)
            break
        else:
            seq.append(circleRocks)

    cycle_start = seq[:-1].index(seq[-1])
    seq.pop()
    cycle_len = len(seq) - cycle_start
    starting_parts = len(seq) - cycle_len
    res = (1000000000-starting_parts) % cycle_len + starting_parts
    circleRocks = seq[res]

    return circleRocks

with open("input.txt") as f:
    graph = list(f.read().strip().split('\n'))
    # print(parse(graph))
    print(calculate_score(shift_rocks(graph), len(graph)))