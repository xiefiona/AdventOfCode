
def dist(nodex, nodey, row_weights, col_weights):
    xrow, xcol = nodex
    yrow, ycol = nodey
    return sum(row_weights[min(xrow, yrow):max(xrow, yrow)]) + sum(col_weights[min(xcol, ycol):max(xcol, ycol)])

def shortest_path(graph):
    # make expansions and build the graph data structure
    row_weights = [1 if '#' in line else 1000000 for line in graph]
    col_weights = [1000000] * len(graph[0])
    for col in range(len(graph[0])):
        for row in range(len(graph)):
            if graph[row][col] == '#':
                col_weights[col] = 1
                break
            
    node_locations = [(row, col) for row in range(len(graph)) for col in range(len(graph[0])) if graph[row][col] == '#']

    distances = []
    for i, nx in enumerate(node_locations):
        for ny in node_locations[i+1:]:
            distances.append(dist(nx,ny, row_weights, col_weights))
    return sum(distances)

with open("input.txt") as f:
    graph = list(map(lambda x: list(x.strip()), f.readlines()))
    print(shortest_path(graph))
    