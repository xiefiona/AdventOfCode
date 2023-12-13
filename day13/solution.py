import numpy as np

def off_by_one(l1,l2):
    if len(l1) != len(l2):
        return False
    diff = False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            if diff:
                return False
            diff = True

    return diff

def valid(graph, ind, numMistakes):
    l, r = ind, ind + 1
    mistakes = 0
    while 0 <= l and r < len(graph):
        if tuple(graph[l]) != tuple(graph[r]):
            if off_by_one(graph[l], graph[r]):
                mistakes += 1
            else:
                return False
        l -= 1
        r += 1
    
    return mistakes == numMistakes

def parse(graph, orientation, part):
    if orientation == 'vert':
        graph = np.transpose(graph)
    mistakes = 1 if part == 2 else 0

    for i in range(len(graph)-1):
        if valid(graph, i, numMistakes=mistakes):
            return (i + 1)
        
    return 0

with open("input.txt") as f:
    graphs = [list(map(list, line.split('\n'))) for line in f.read().split('\n\n')]
    hoz = [parse(graph, 'hoz', 2) for graph in graphs]
    vert = [parse(graph, 'vert', 2) for graph in graphs]
    print(sum(vert) + (100*sum(hoz)))
