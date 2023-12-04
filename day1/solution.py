num_to_spelling_dict = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

def decode(message):
    firstNum, lastNum = None, None
    for i in range(len(message)):
        let = message[i]
        if let.isnumeric():
            lastNum = let
            if not firstNum:
                firstNum = let
        else:
            for potential_num, potential_spelling in num_to_spelling_dict.items():
                if i + len(potential_spelling) < len(message) and message[i:i+len(potential_spelling)] == potential_spelling:
                    lastNum = potential_num
                    if not firstNum:
                        firstNum = potential_num
                    break
    return int(firstNum + lastNum)

ans = 0
with open("input.txt") as f:
    for message in f:
        ans += decode(message)

print(ans)