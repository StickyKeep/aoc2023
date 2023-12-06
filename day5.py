with open("input.in", "r") as f:
    maps = []
    seeds = [int(x) for x in f.readline().split(": ")[1].split()]
    
    for line in f:
        line = line.strip("")
        if line == "\n":
            continue
        if line.endswith("map:\n"):
            continue
        else:
            maps.append([int(x) for x in line.split()])


print(seeds)
print(maps)

# \n
