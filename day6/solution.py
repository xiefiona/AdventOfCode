
def num_ways(time, dist):
    ways = 0
    for i in range(time):
        if i * (time-i) > dist:
            ways += 1
    return ways

with open("input.txt") as f:
    lines = f.readlines()
    # times = list(map(int,lines[0].split()[1:]))
    # distances = list(map(int,lines[1].split()[1:]))
    times = [int(''.join(lines[0].split()[1:]))]
    distances = [int(''.join(lines[1].split()[1:]))]
    
    pairs = zip(times, distances)

    ans = 1
    for (time, dist) in pairs:
        ans *= num_ways(time, dist)

    print(ans)
