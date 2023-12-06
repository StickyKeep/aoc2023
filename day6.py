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
            

