
def bfs(graph, start):
    energized = set()

    curr = [start] # (x,y, xdiff, ydiff)
    while curr:
        next = []
        for r,c,rdiff,cdiff in curr:
            if (r,c,rdiff,cdiff) in energized:
                continue
            if 0 <= r < len(graph) and 0 <= c < len(graph[r]):
                energized.add((r,c,rdiff,cdiff))
                currstate = graph[r][c]
                if currstate == '.':
                    next.append((r+rdiff, c+cdiff, rdiff, cdiff))
                elif currstate == '|':
                    if cdiff == 0:
                        next.append((r+rdiff, c+cdiff, rdiff, cdiff))
                    else:
                        next.append((r+1, c, 1, 0))
                        next.append((r-1, c, -1, 0))
                elif currstate == '-':
                    if rdiff == 0:
                        next.append((r+rdiff, c+cdiff, rdiff, cdiff))
                    else:
                        next.append((r, c+1, 0, 1))
                        next.append((r, c-1, 0, -1))
                elif currstate == '/':
                    if rdiff == 1: # down (1,0) -> (0,-1)
                        next.append((r, c-1, 0, -1))
                    elif rdiff == -1: # up
                        next.append((r, c+1, 0, 1))
                    elif cdiff == 1: # right
                        next.append((r-1, c, -1, 0))
                    elif cdiff == -1: #left
                        next.append((r+1, c, 1, 0))
                    else:
                        assert False, "/ logic error"

                elif currstate == '\\':
                    if rdiff == 1: #(1,0) -> (0,-1)
                        next.append((r, c+1, 0, 1))
                    elif rdiff == -1:
                        next.append((r, c-1, 0, -1))
                    elif cdiff == 1:
                        next.append((r+1, c, 1, 0))
                    elif cdiff == -1:
                        next.append((r-1, c, -1, 0))
                    else:
                        assert False, "\ logic error"
                else:
                    assert False
        curr = next

    ans = set(map(lambda x: (x[0], x[1]), energized))
    return ans

with open("input.txt") as f:
    graph = f.read().strip().split('\n')
    print(len(bfs(graph,(0,0,0,1)))) # part 1

    top = max([len(bfs(graph, (0,col,1,0))) for col in range(len(graph[0]))])
    bottom = max([len(bfs(graph, (len(graph)-1,col,-1,0))) for col in range(len(graph[0]))])
    left = max([len(bfs(graph, (row,0,0,1))) for row in range(len(graph))])
    right = max([len(bfs(graph, (row,len(graph[0])-1,0,-1))) for row in range(len(graph))])
    print(max(top, bottom, left, right)) # part 2
