# https://adventofcode.com/2023/day/6

with open("input.in", "r") as f:
    times = [int(x) for x in f.readline().split(": ")[1].split()]
    distance = [int(x) for x in f.readline().split(": ")[1].split()]

print(times, distance)

number_of_wins = 1

for i, time in enumerate(times):
    wins = 0
    for seconds_pressed in range(1, time):
        distance1 = (time - seconds_pressed) * seconds_pressed
        if distance1 > distance[i]:
            wins += 1
    number_of_wins *= wins

print(number_of_wins)
            
# Copy paste and reuse for part 2: 
# "There's really only one race - ignore the spaces between the numbers on each line."

time = int(''.join(map(str, times)))
distance = int(''.join(map(str, distance)))

wins2 = 0
for seconds_pressed in range(1, time):
    distance2 = (time - seconds_pressed) * seconds_pressed
    if distance2 > distance:
        wins2 += 1

print(wins2)    
    
# 138915
# 27340847
