
import polars as pl
with open('input.in') as f:
    content = [x.strip() for x in f.readlines()]

nums = {"one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
# Part 1:

part_1_sum = 0

for line in content:
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)
    part_1_sum += int(digits[0] + digits[-1])

print(f"Part 1 sum: {part_1_sum}")

# Part 2:


def find_digits(s, number_dict, reverse=False):
    if reverse == False:
        for i in range(len(s)):
            if s[i].isdigit():
                return str(s[i])
            else:
                for number, value in number_dict.items():
                    if s[i:].startswith(number):
                        return str(value)
    else:
        for i in range(len(s))[::-1]:
            if s[i].isdigit():
                return str(s[i])
            else:
                for number, value in number_dict.items():
                    if s[i:].startswith(number):
                        return str(value)


part_2_sum = 0

for line in content:
    n1 = find_digits(line, nums)
    n2 = find_digits(line, nums, reverse=True)
    part_2_sum += int(n1 + n2)

print(f"Part 2 sum: {part_2_sum}")

# Solution using Polars:

pldf = pl.read_csv(
    "input.in", has_header=False)
plseries = pldf.to_series()

# We can just replace the written out number to one that includes the digit in the middle
# This handles cases where they overlap, for example like "twone", and we can just do
# a simple isdigit() check to find the first and last.

masking = {"one": "o1ne", "two": "tw2o", "three": "thr3e", "four": "fo4ur",
           "five": "fi5ve", "six": "si6x", "seven": "sev7en", "eight": "eig8ht", "nine": "n9ine"}

for key, value in masking.items():
    plseries = plseries.str.replace_all(key, value)

polar_sum = 0

for line in plseries:
    first_digit = None
    last_digit = None

    # Find first and last digit
    for char in line:
        if char.isdigit():
            first_digit = char
            # Then we put it in reverse
            for char_r in line[::-1]:
                if char_r.isdigit():
                    last_digit = char_r
                    break
            break

    polar_sum += int(first_digit + last_digit)

print(f"With polars: {polar_sum}")

# Part 1 sum: 53921
# Part 2 sum: 54676
# With polars: 54676
