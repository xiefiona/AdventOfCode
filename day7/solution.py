from collections import Counter

hand_ranks = [(1,1,1,1,1), (2,1,1,1), (2,2,1), (3,1,1), (3,2), (4,1), (5,)]
ranking_map = {
    '2': 0.02,
    '3': 0.03,
    '4': 0.04,
    '5': 0.05,
    '6': 0.06,
    '7': 0.07,
    '8': 0.08,
    '9': 0.09,
    'T': 0.10,
    'J': 0.11,
    'Q': 0.12,
    'K': 0.13,
    'A': 0.14
}
ranking_map_2 = {
    '2': 0.02,
    '3': 0.03,
    '4': 0.04,
    '5': 0.05,
    '6': 0.06,
    '7': 0.07,
    '8': 0.08,
    '9': 0.09,
    'T': 0.10,
    'J': 0.01,
    'Q': 0.12,
    'K': 0.13,
    'A': 0.14
}

def part_1_sol(lines):
    lines = [tuple(line) for line in lines]
    card_hand_types = {}
    for (hand, bid) in lines:
        hand_type = tuple(sorted(dict(Counter(hand)).values(), reverse=True))
        if hand_type not in card_hand_types:
            card_hand_types[hand_type] = []
        card_hand_types[hand_type].append((hand, int(bid)))

    sorted_hands = []
    for hand_type in hand_ranks:
        if hand_type in card_hand_types:
            cards = [list(map(lambda x: ranking_map[x], list(hand))) for hand, _ in card_hand_types[hand_type]]
            bids = [bid for _, bid in card_hand_types[hand_type]]

            assert(len(cards) == len(bids))
            new_card_representation = [tuple(cards[i] + [bids[i]]) for i in range(len(cards))]

            sorted_hands.extend(sorted(new_card_representation))

    ans = 0
    for rank, representation in enumerate(sorted_hands):
        ans += ((rank+1) * representation[-1])
    return ans

def part_2_sol(lines):
    lines = [tuple(line) for line in lines]
    card_hand_types = {}
    for (hand, bid) in lines:
        counts = dict(Counter(hand))
        if 'J' in counts.keys():
            maxlet = None
            for let, freq in counts.items():
                if let != 'J' and (maxlet is None or freq >= counts[maxlet]):
                    maxlet = let
            
            if maxlet is not None:
                counts[maxlet] += counts['J']
                del counts['J']
        hand_type = tuple(sorted(counts.values(), reverse=True))

        if hand_type not in card_hand_types:
            card_hand_types[hand_type] = []
        card_hand_types[hand_type].append((hand, int(bid)))

    sorted_hands = []
    for hand_type in hand_ranks:
        if hand_type in card_hand_types:
            cards = [list(map(lambda x: ranking_map_2[x], list(hand))) for hand, _ in card_hand_types[hand_type]]
            bids = [bid for _, bid in card_hand_types[hand_type]]

            assert(len(cards) == len(bids))
            new_card_representation = [tuple(cards[i] + [bids[i]]) for i in range(len(cards))]

            sorted_hands.extend(sorted(new_card_representation))

    ans = 0
    # print(sorted_hands)
    for rank, representation in enumerate(sorted_hands):
        ans += ((rank+1) * representation[-1])
    return ans

with open("input.txt") as f:
    lines = [line.split() for line in f.readlines()]

    print(part_2_sol(lines))