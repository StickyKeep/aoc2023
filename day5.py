import time
with open("input.in", "r") as f:
    seeds = [int(x) for x in f.readline().split(": ")[1].split()]
    map_of_maps = []
    current_map = []

    for line in f:
        line = line.strip()
        if line == "":
            map_of_maps.append(current_map)
            current_map = []
        elif "map:" in line:
            continue
        else:
            current_map.append([int(x) for x in line.split()])
    map_of_maps.append(current_map)

seeds2 = seeds.copy() # For part 2

def find_mapped_value(num, map):
    for entry in map:
        dest_start, src_start, length = entry
        if src_start <= num < src_start + length:
            return dest_start + (num - src_start)
    return num  


final_values = []
for seed in seeds:
    current_value = seed
    for map in map_of_maps:
        current_value = find_mapped_value(current_value, map)
    final_values.append(current_value)

print(min(final_values))

# Part 2.
# When in doubt, bruteforce out:

with open("input.in", "r") as f:
    seeds = [int(x) for x in f.readline().split(": ")[1].split()]
    map_of_maps = []
    current_map = []

    for line in f:
        line = line.strip()
        if line == "":
            map_of_maps.append(current_map)
            current_map = []
        elif "map:" in line:
            continue
        else:
            current_map.append([int(x) for x in line.split()])
    map_of_maps.append(current_map)

start_time = time.time()

final_values2 = []
for i in range(0, len(seeds2), 2):
    start = seeds2[i]
    range_length = seeds2[i + 1]
    for j in range(start, start + range_length):
        current_value = j
        for map in map_of_maps:
            current_value = find_mapped_value(current_value, map)
        final_values2.append(current_value)

print(min(final_values2))

end_time = time.time()

execution_time = end_time - start_time
print("Execution time: {:.2f} seconds".format(execution_time))

# Killed my Mac using vanilla Python, but worked like a charm in under 30 mins with pypy ¯\_(ツ)_/¯
# 63179500
# Execution time: 1726.30 seconds
        
