
history = {}

def get_arrangements(springs, target):
    if len(target) == 0:
        return 0 if '#' in springs else 1
    if len(springs) == 0:
        return 0
    if (springs, tuple(target)) in history:
        return history[(springs, tuple(target))]

    res = 0
    target_num = target[0]
    for i in range(len(springs)):
        if i + target_num <= len(springs):
            if '.' not in springs[i:i+target_num] and (i+target_num == len(springs) or springs[i+target_num] != '#'):
                res += get_arrangements(springs[i+target_num+1:], target[1:])

        if springs[i] == '#':
            break

    history[(springs, tuple(target))] = res
    return res

with open("input.txt") as f:
    lines = list(map(lambda x: x.strip().split(), f.readlines()))
    
    # arrangements = [get_arrangements(line[0], list(map(int, line[1].split(',')))) for line in lines]
    arrangements = [get_arrangements('?'.join([line[0]]*5), list(map(int, line[1].split(',')))*5) for line in lines]
    print(sum(arrangements))
