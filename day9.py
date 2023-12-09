with open("input.in") as f:
    nums = [list(map(int,line.strip().split())) for line in f]



def find_differences(nums_list):
    if all(number == 0 for number in nums_list):
        return 0
    differences = [y- x for x, y in zip(nums_list, nums_list[1:])]
    difference = find_differences(differences)
    return nums_list[-1] + difference

sum = 0
for going_out_of_variable_names in nums:
    sum += find_differences(going_out_of_variable_names)

print(sum)