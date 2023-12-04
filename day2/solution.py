max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def decode_part_1(message):
    gameid_str, handfulls = message.split(':')
    game_num = int(gameid_str.split(' ')[1])

    for handfull in handfulls.split(';'):
        cubes = handfull.split(',')
        
        for cube in cubes:
            num, color = cube.strip().split(' ')
            if max_cubes[color] < int(num):
                return 0
    
    return game_num

def decode_part_2(message):
    _, handfulls = message.split(':')

    config = {}

    for handfull in handfulls.split(';'):
        cubes = handfull.split(',')
        
        for cube in cubes:
            num, color = cube.strip().split(' ')
            if color not in config:
                config[color] = int(num)
            config[color] = max(config[color], int(num))
    
    product = 1
    for val in config.values():
        product *= val
    return product
    
ans = 0
with open("input.txt") as f:
    for message in f:
        ans += decode_part_2(message)

print(ans)