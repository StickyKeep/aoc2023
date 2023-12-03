with open("in.in", "r") as f:
    data = f.read().splitlines()

coordinates_map = set()

# Make coordinate map for special characters:
for row, line in enumerate(data):
    for col, char in enumerate(line):
        if char == "." or char.isdigit():
            continue
        coordinates_map.add((row, col))

row_len = len(data)
col_len = len(data[0])
potential_number = ""
total_sum = 0

# Iterate through grid and find potential numbers
# Check if surrounding cells have special characters
# If yes, add number to total sum
for row, line in enumerate(data):
    i = 0
    while i < col_len:
        potential_number = ""
        while i < col_len and line[i].isdigit():
            potential_number += str(line[i])
            i += 1

        if potential_number:
            #print(row, i, potential_number)
            number = int(potential_number)
            number_length = len(potential_number)
            found_symbol = False
            rightmost_index = i
            leftmost_index = i - number_length

            for r in range(row-1, row+2):
                for c in range(leftmost_index-1, i+1):
                    if (r, c) in coordinates_map:
                        total_sum += number
                        found_symbol = True
                        break
                if found_symbol:
                    break

            potential_number = ""

        i += 1

print(f"Part 1 sum: {total_sum}")


# Copy paste for solution for part 2:

# Use two dictionaries to keep track of the multiplication and the number of times a cell has been multiplied
# If a cell has been multiplied twice, i.e. the coordinate is adjacent to two numbers, add it to the total sum
coordinates_map_dict = {}
coordinates_map_dict_multiplication_counter = {}

# Map coordinates for "*"
for row, line in enumerate(data):
    for col, char in enumerate(line):
        if char == "*":
            coordinates_map_dict[row, col] = 1 # For the multiplication of first found number
            coordinates_map_dict_multiplication_counter[row, col] = 0 # To keep track of # of multiplications

row_len = len(data)
col_len = len(data[0])
potential_number = ""
total_sum = 0

# Iterate through grid and find potential numbers
# Check if surrounding cells have a "*"
for row, line in enumerate(data):
    i = 0
    while i < col_len:
        potential_number = ""
        while i < col_len and line[i].isdigit():
            potential_number += str(line[i])
            i += 1

        if potential_number:
            number = int(potential_number)
            number_length = len(potential_number)
            found_symbol = False
            rightmost_index = i
            leftmost_index = i - number_length

            for r in range(row-1, row+2):
                for c in range(leftmost_index-1, i+1):
                    if (r, c) in coordinates_map_dict:
                        coordinates_map_dict[(r, c)] *= number
                        coordinates_map_dict_multiplication_counter[(r, c)] += 1
                        found_symbol = True
                        break
                if found_symbol:
                    break

            potential_number = ""

        i += 1

for key, value in coordinates_map_dict.items():
    if coordinates_map_dict_multiplication_counter[key] == 2:
        total_sum += value

print(f"Part 2 sum: {total_sum}")