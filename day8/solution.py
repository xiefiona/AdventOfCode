let_map = {}

from math import gcd # Python versions 3.5 and above
#from fractions import gcd # Python versions below 3.5
from functools import reduce # Python version 3.x

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

def get_num_steps_new(commands, connections):
    curr_elems = []
    for c in connections:
        parts = c.split(' = ')
        let_map[parts[0]] = tuple(parts[1].strip('()').replace(',','').split())
        if parts[0][-1] == 'A':
            curr_elems.append(parts[0])

    return lcm([get_num_steps_helper(elem, commands) for elem in curr_elems])

def get_num_steps_helper(elem, commands):
    num_steps = 0
    curr_elem = elem
    ind = 0
    while curr_elem[-1] != 'Z':
        curr_command = 0 if commands[ind] == 'L' else 1
        curr_elem = let_map[curr_elem][curr_command]
        
        ind += 1
        if ind >= len(commands):
            ind = 0
        num_steps += 1

    return num_steps

def get_num_steps(commands, connections):
    for c in connections:
        parts = c.split(' = ')
        let_map[parts[0]] = tuple(parts[1].strip('()').replace(',','').split())

    num_steps = 0
    curr_elem = 'AAA'
    ind = 0
    while curr_elem != 'ZZZ':
        curr_command = 0 if commands[ind] == 'L' else 1
        curr_elem = let_map[curr_elem][curr_command]
        
        ind += 1
        if ind >= len(commands):
            ind = 0
        num_steps += 1

    return num_steps

def get_num_steps_part_2(commands, connections):
    curr_elems = []
    for c in connections:
        parts = c.split(' = ')
        let_map[parts[0]] = tuple(parts[1].strip('()').replace(',','').split())
        if parts[0][-1] == 'A':
            curr_elems.append(parts[0])

    num_steps = 0
    ind = 0
    while any([c[-1] != 'Z' for c in curr_elems]):
        curr_command = 0 if commands[ind] == 'L' else 1
        curr_elems = [let_map[elem][curr_command] for elem in curr_elems]
        
        ind += 1
        if ind >= len(commands):
            ind = 0
        num_steps += 1

    return num_steps

with open("input.txt") as f:
    lines = f.read().split('\n\n')
    commands = lines[0] 
    connections = lines[1].strip().split('\n')

    print(get_num_steps_new(commands, connections))
