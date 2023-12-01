# Rewritten to only find first and last number
# Still very spaghetti :) 

with open('input.in') as f:
    content = [x.strip() for x in f.readlines()]

nums = {"one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

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
                    
total_sum = 0

for line in content:
    n1 = find_digits(line, nums)
    print(n1)
    n2 = find_digits(line, nums, reverse=True)
    print(n2)
    total_sum += int(n1 + n2)

print(total_sum)

# Ans: 54676


