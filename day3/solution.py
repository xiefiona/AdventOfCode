"""
Solution Overview: Search for all numbers in the grid, then for each number represented by (row, start_col, end_col) we 
look in all 8 adjacent locations for a symbol and if a symbol is found, we increment the total based on the point
counting scheme for each part.

gears is used in part 2 and represents a mapping from each * location to a list of all numbers that are adjacent to it

Runtime of each part is in O(NM) where N is the number of rows, M is the number of columns

Note: [start_col, end_col) is inclusive, exclusive 
"""

gears = {}

def increment(table, row, end_col):
    if end_col >= len(table[row]):
        return row + 1, 0

    return row, end_col

def check_boundaries(table, row, start_col, end_col):
    added_gears = set()
    for col in range(start_col, end_col):
        for rowdiif, coldiff in [(-1,0), (1,0), (-1,-1), (1,1), (0,1), (0,-1), (-1,1), (1,-1)]:
            newrow, newcol = row + rowdiif, col + coldiff
            if 0 <= newrow < len(table) and 0 <= newcol < len(table[newrow]):
                char = table[newrow][newcol]
                if char == "*":
                # if not char.isdigit() and char != '.':
                    if (newrow, newcol) not in gears:
                        gears[(newrow, newcol)] = []
                    if (newrow, newcol) not in added_gears:
                        gears[(newrow, newcol)].append(int(''.join(table[row][start_col:end_col])))
                        added_gears.add((newrow, newcol))

def parse(table):
    row, start_col = 0, 0 # inclusive, exclusive

    while row < len(table): 
        end_col = start_col + 1
        if table[row][start_col].isdigit():
            while end_col < len(table[row]) and table[row][end_col].isdigit():
                end_col += 1
            check_boundaries(table, row, start_col, end_col)
                # ressum += int(''.join(table[row][start_col:end_col]))

        row, start_col = increment(table, row, end_col)

    ans = 0
    print(gears)
    for gear in gears.values():
        if len(gear) == 2:
            ans += (gear[0] * gear[1])
    return ans

table = []

with open("day3input.txt") as f:
    for message in f.readlines():
        message = message.strip()
        mess = []
        for char in message:
            mess.append(char)

        table.append(mess)


    print(parse(table))