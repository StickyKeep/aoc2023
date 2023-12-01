with open('day1_input.txt') as f:
    content = [x.strip() for x in f.readlines()]

nums = {"one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

sum = 0

for line in content:
    string = ""
    i = 0
    while i < len(line):
        if line[i].isdigit():
            string += str(line[i])
            i += 1
        else:
            for number, value in nums.items():
                if line[i:].startswith(number):
                    string += str(value)
                    i += 1

            else:
                i += 1

    sum += int(string[0] + string[-1])

print(sum)
