
pipe_map = {
    '|': [(-1,0), (1,0)],
    '-': [(0,-1), (0,1)],
    'L': [(-1,0), (0,1)],
    'J': [(-1,0), (0,-1)],
    '7': [(1,0), (0,-1)],
    'F': [(1,0), (0,1)],
    'S': [(-1,0), (1,0), (0,-1), (0,1)],
    '.': []
}

start_map = {
    (-1,0): ['|', '7', 'F'],
    (1,0): ['|', 'J', 'L'],
    (0,1): ['-', '7', 'J'],
    (0,-1): ['-', 'L', 'F']
}

hoz = [('-','-'), ('-','7'), ('-','J'), ('L','-'), ('F','-'), ('L', 'J')]

def get_start_pos(graph):
    for row in range(len(graph)):
        for col in range(len(graph[row])):
            if graph[row][col] == 'S':
                return (row,col)

def part_two(seen, graph):
    spos = get_start_pos(graph)
    big_graph_cycle = set([(2*x+1, 2*y+1) for x,y in seen])
    graph[spos[0]][spos[1]] = '|'
    # graph[spos[0]][spos[1]] = 'F'

    # double to width and height, align stuff in the rows and columns
    big_graph = [['.'] * (2 * len(graph) + 1)]
    for row in range(len(graph)):
        expanded_row = ['.']
        blank_row = ['.'] * (2 * len(graph[0]) + 1)
        for col in range(len(graph[row])):
            expanded_row.append(graph[row][col])
            expanded_row.append('.')
            if col+1 < len(graph[row]) and (row, col) in seen and (row, col+1) in seen:
                if graph[row][col] in ['-', 'F', 'L'] and graph[row][col+1] in ['-', 'J', '7']:
                    expanded_row[-1] = '-'
                    big_graph_cycle.add((2*row+1,2*(col+1)))
            if row+1 < len(graph) and (row, col) in seen and (row+1, col) in seen:
                if graph[row][col] in ['|', 'F', '7'] and graph[row+1][col] in ['|', 'L', 'J']:
                    blank_row[2*col + 1] = '|'
                    big_graph_cycle.add((2*(row+1),2*col+1))
                
        big_graph.append(expanded_row)
        big_graph.append(blank_row)

    # bfs to find number of searched
    is_outside_seen = set()
    small_outside_seen = set()
    startPos = [(0,0)]
    
    while len(startPos) > 0:
        newPos = []
        for r, c in startPos:
            if (r,c) not in is_outside_seen:
                big_graph[r][c] = 'O'
                is_outside_seen.add((r,c))
                if r % 2 == 1 and c % 2 == 1:
                    small_outside_seen.add(((r-1)//2, (c-1)//2))
                for rdiff, cdiff in [(0,1), (0,-1), (1,0), (-1,0)]:
                    if 0 <= r + rdiff < len(big_graph) and 0 <= c + cdiff < len(big_graph[r+rdiff]):
                        if (r+rdiff, c+cdiff) not in big_graph_cycle:
                            newPos.append((r+rdiff, c+cdiff))
                            
        startPos = newPos
    
    # find number of things from original grid that weren't accessed during flood and also aren't in the cycle
    return sum([(r,c) not in seen and (r,c) not in small_outside_seen for r in range(len(graph)) for c in range(len(graph[0]))])

def bfs(graph):
    spos = get_start_pos(graph)
    startPos = []
    seen = set()
    seen.add(spos)

    for rdiff, cdiff in [(-1,0), (1,0), (0,1), (0,-1)]:
        newr, newc = spos[0] + rdiff, spos[1] + cdiff
        if 0 <= newr < len(graph) and 0 <= newc < len(graph[newr]): 
            if graph[newr][newc] in start_map[(rdiff, cdiff)]:
                startPos.append((newr, newc))

    depth = 1
    final_graph = [[-1]*len(line) for line in graph]
    while len(startPos) > 0:
        newPos = []
        for r, c in startPos:
            if (r,c) not in seen:
                final_graph[r][c] = depth
                seen.add((r,c))
                for rdiff, cdiff in pipe_map[graph[r][c]]:
                    if 0 <= r + rdiff < len(graph) and 0 <= c + cdiff < len(graph[r+rdiff]):
                        if (r+rdiff, c+cdiff) not in seen:
                            newPos.append((r+rdiff, c+cdiff))
                            
        assert len(startPos) == 2, f"depth {depth}: {startPos}"
        startPos = newPos
        depth += 1

    return seen, max(final_graph[r][c] for r in range(len(final_graph)) for c in range(len(final_graph[0])))

with open("input.txt") as f:
    graph = list(map(lambda x: list(x.strip()), f.readlines()))
    cycle, maxlen = bfs(graph)
    # print(maxlen)
    print(part_two(cycle, graph))
