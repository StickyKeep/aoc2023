with open("input.in") as f:
    nums = [list(map(int, line.strip().split())) for line in f]


def find_differences(nums_list):
    if all(number == 0 for number in nums_list):
        return 0
    differences = [y - x for x, y in zip(nums_list, nums_list[1:])]
    difference = find_differences(differences)
    return nums_list[-1] + difference

sum = 0

# Iterate over input numbers:
for running_out_of_variable_names in nums:
    sum += find_differences(running_out_of_variable_names)

print(f"Part 1 sum: {sum}")


# Part 2: Just need to make small adjustment in find_differences() from pt. 1:

def find_differences_pt2(nums_list):
    if all(number == 0 for number in nums_list):
        return 0
    differences = [y - x for x, y in zip(nums_list, nums_list[1:])]
    difference = find_differences_pt2(differences)
    return nums_list[0] - difference

sum = 0

for running_out_of_variable_names in nums:
    sum += find_differences_pt2(running_out_of_variable_names)

print(f"Part 2 sum: {sum}")
