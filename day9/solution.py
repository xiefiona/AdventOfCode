
# hsitory is a list of integers
def calculate(history, part):
    pyramid = [history]
    while any([p != 0 for p in pyramid[-1]]):
        diff = [pyramid[-1][i] - pyramid[-1][i-1] for i in range(1,len(pyramid[-1]))] if len(pyramid[-1]) > 1 else [0]
        # print(diff)
        pyramid.append(diff)

    if part == 1:
        return sum([x[-1] for x in pyramid])
    else:
        res = 0
        for x in reversed(pyramid):
            res = x[0] - res
        return res

with open("input.txt") as f:
    pred = [calculate(list(map(int,line.split()))) for line in f.readlines()]
    print(sum(pred))
