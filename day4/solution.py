valid_cards = {}

def calculate(message):
    nums = message.split(':')[1].split('|')
    winning_nums = set(nums[0].strip().split())
    my_nums = set(nums[1].strip().split())

    matching_nums = winning_nums.intersection(my_nums)
    if len(matching_nums) > 0:
        return 1 << len(matching_nums) - 1
    return 0

def calculate_part_2(message):
    card_num = int(message.split(':')[0].split()[1])
    nums = message.split(':')[1].split('|')
    winning_nums = set(nums[0].strip().split())
    my_nums = set(nums[1].strip().split())

    matching_nums = winning_nums.intersection(my_nums)
    
    if card_num not in valid_cards:
        valid_cards[card_num] = 0
    valid_cards[card_num] += 1

    for i in range(len(matching_nums)):
        copy_card = card_num + i + 1
        if copy_card not in valid_cards:
            valid_cards[copy_card] = 0
        valid_cards[copy_card] += valid_cards[card_num]
    
ans = 0
with open("input.txt") as f:
    for message in f:
        ans += calculate(message.strip())
        calculate_part_2(message.strip())

# print(ans)
print(sum(valid_cards.values()))