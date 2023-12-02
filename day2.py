
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

print(tsum)

# 2169


