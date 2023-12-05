def parse(input, part_two=True):
    lines = input.strip().split('\n')
    seeds = list(map(int, lines[0].split(':')[1].strip().split()))
    if part_two:
        seeds = [(seeds[2*i], seeds[(2*i)+1]) for i in range(len(seeds) // 2)]
    mapping = {}
    
    ind = 1
    while ind < len(lines):
        if ":" in lines[ind]:
            mapname = lines[ind].split(' ')[0].split('-')

            ranges = []
            ind += 1
            while ind < len(lines) and lines[ind] != "":
                num_map = tuple(map(int, lines[ind].strip().split()))
                ranges.append((num_map[1], num_map[0], num_map[2]))
                ind += 1
            ranges.sort()
            mapping[mapname[0]] = (mapname[2], ranges)
        else:
            ind += 1 # case where there is an empty line

    return seeds, mapping   

def get_location(seed, mapping):
    name = "seed"
    num = seed
    while name != "location":
        new_name, curr_map_list = mapping[name]

        for source_start, dest_start, length in curr_map_list:
            if source_start <= num < source_start + length:
                num = dest_start + (num - source_start)
                break
        
        name = new_name
        
    return num

def get_map_value(num, map):
    for source_start, dest_start, length in map:
        if source_start <= num < source_start + length:
            return dest_start + (num - source_start), length - (num - source_start)
        elif num < source_start:
            return num, source_start - num
        
    return num, None

def get_locations(source_name, source_list, mapping):
    if source_name == "location":
        return source_list
    
    ans = []
    new_source_name, curr_map = mapping[source_name]
    for source_start, length in source_list:
        curr_num = source_start
        new_source_list = []
        # get new values using the curr_map
        while curr_num < source_start + length:
            new_num, new_len = get_map_value(curr_num, curr_map)
            if new_len == None or curr_num + new_len > source_start + length:
                new_len = source_start + length - curr_num    # 1 -> 2, 2 (source start + len = 2)
            new_source_list.append((new_num, new_len))
            curr_num += new_len

        assert(curr_num == source_start + length)
        
        curr_results = get_locations(new_source_name, new_source_list, mapping)
        ans.extend(curr_results)
    return ans

with open("input.txt") as f:
    input = f.read()
    seeds, mapping = parse(input, True)

    # locations = [get_location(seed, mapping) for seed in seeds]
    locations = get_locations("seed", seeds, mapping)

    # print(min(locations))
    print(min(locations)[0])
