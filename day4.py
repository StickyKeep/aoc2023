from collections import defaultdict

with open("input.in", "r") as f:
    data = [line.strip().split(":")[1].split("|") for line in f.readlines()]

tsum = 0

for line in data:
    # Use sets to check if our game has any of the winning numbers
    winning = set(line[0].split())
    game = set(line[1].split())
    winning = winning.intersection(game)
    tsum += (2**(len(winning)-1)) if len(winning) > 0 else 0

print(tsum)

# Part 2: 
# This time map each card to the number of times we get it

winning_cards = defaultdict(int)

for card, line in enumerate(data, 1):
    if card not in winning_cards:
        winning_cards[card] = 1

    winning_numbers = set(line[0].split())
    game = set(line[1].split())
    won = winning_numbers.intersection(game)

    if len(won):
        for i in range(card + 1, card + len(won) + 1):
            winning_cards[i] = winning_cards.get(i,1) + winning_cards[card]

print(sum(winning_cards.values()))

# 33950
# 14814534
