# gogo

with open('day1_input.txt') as f:
    content = [x.strip() for x in f.readlines()]

sum = 0
string = ""

content2 = []


for line in content:
    ints = []
    for i in line: 
        try:
            int(i)
            ints.append(i)
        except ValueError:
            pass
    content2.append(ints)

for numbs in content2:
    sum += int(numbs[0] + numbs[-1])

print(sum)

