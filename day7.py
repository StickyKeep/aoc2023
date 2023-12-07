games = []

with open("in.in", "r") as f:
    for line in f:
        hand, bid = line.strip().split(" ")
        games.append((hand, int(bid)))

print(games)
