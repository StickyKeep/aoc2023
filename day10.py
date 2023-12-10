# https://adventofcode.com/2023/day/10

from collections import deque

with open("in.in") as f:
    gridworld = f.read().strip().splitlines()

# Find starting position S:
# s_R, s_C = 0, 0

for row, column, in enumerate(gridworld):
    for col, char in enumerate(column):
        if char == "S":
            s_R = row
            s_C = col

# Define pipes:


right = "S-LF"
left = "S-J7"
down = "S|7F"
up = "S|JL"

# Pretty standard BFS from here in part 1:

seen = {(s_R, s_C)}
queue = deque([(s_R, s_C)])

while queue:
    r, c = queue.popleft()
    char = gridworld[r][c]
    if r > 0 and char in up and gridworld[r-1][c] in down[1:]:
        if (r-1, c) not in seen:
            queue.append((r-1, c))
            seen.add((r-1, c))
    if r < len(gridworld)-1 and char in down and gridworld[r+1][c] in up[1:]:
        if (r+1, c) not in seen:
            queue.append((r+1, c))
            seen.add((r+1, c))
    if c > 0 and char in left and gridworld[r][c-1] in right[1:]:
        if (r, c-1) not in seen:
            queue.append((r, c-1))
            seen.add((r, c-1))
    if c < len(gridworld[0])-1 and char in right and gridworld[r][c+1] in left[1:]:
        if (r, c+1) not in seen:
            queue.append((r, c+1))
            seen.add((r, c+1))

print(len(seen)//2)

# Part 2: TBA