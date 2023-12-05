with open("input.in", "r") as f:
    seeds = [int(x) for x in f.readline().split(": ")[1].split()]

print(seeds)