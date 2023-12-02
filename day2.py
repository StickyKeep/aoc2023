
with open('input.in') as f:
    data = [[group.split(", ") for group in x.strip().split(': ')[
        1].split("; ")] for x in f.readlines()]

tsum = 0

for game, groups in enumerate(data, 1):
    
    for group in groups:
        color_map = {"red": 0, "green": 0, "blue": 0}
        for pair in group:
            num, color = pair.split()
            color_map[color] += int(num)
            if color_map["red"] > 12 or color_map["green"] > 13 or color_map["blue"] > 14:
                break
        else:
            continue
        break
    else:
        tsum += game


# Quick copy paste and edit for part 2,
# to find the minimum numbers of each color needed for each game

power_sum = 0 

for game, groups in enumerate(data, 1):
    color_map = {"red": 0, "green": 0, "blue": 0}
    for group in groups:
        
        for pair in group:
            num, color = pair.split()
            if color_map[color] < int(num):
                color_map[color] = int(num)
    r, g, b = color_map.values()
    power_sum += r * g * b


print(f"Sum of indexes of possible games: {tsum}")
print(f"Power sum of minimum number of colors needed: {power_sum}")

# 2169
# 60948

