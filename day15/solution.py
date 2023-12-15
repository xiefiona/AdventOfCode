from collections import defaultdict

def parse(input):
    curr_val = 0
    for char in input:
        curr_val += ord(char)
        curr_val *= 17
        curr_val = curr_val % 256
    return curr_val

def part_2(steps):
    boxes = defaultdict(list) # list of tuples (code, focallen)
    for step in steps:
        if '-' in step:
            label = step[:-1]
            boxnum = parse(label)
            if boxnum in boxes and any([label == l for l,_ in boxes[boxnum]]):
                ind = [i for i, (l, _) in enumerate(boxes[boxnum]) if label == l][0]
                boxes[boxnum].pop(ind)
        else:
            label, focallen = step.split('=')
            boxnum = parse(label)
            if boxnum in boxes and any([label == lab for lab,_ in boxes[boxnum]]):
                ind = [i for i, (l, _) in enumerate(boxes[boxnum]) if label == l][0]
                boxes[boxnum][ind] = (label, int(focallen))
            else:
                boxes[boxnum].append((label, int(focallen)))

    ans = sum([(box+1)*(i+1)*focallen for box, slots in boxes.items() for i, (_,focallen) in enumerate(slots)])
    return ans

with open("input.txt") as f:
    steps = f.read().strip().split(',')
    print(sum([parse(step) for step in steps]))
    print(part_2(steps))
