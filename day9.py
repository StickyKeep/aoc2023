with open("input.in") as f:
    nums = [list(map(int,line.strip().split())) for line in f]

for numbers in nums:
    for n in numbers:
        print(n)