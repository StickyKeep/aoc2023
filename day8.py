import itertools

with open("input.in") as f:
    movements = f.readline().strip()
    f.readline()  # Skip the second line
    graphs = {}
    for line in f:
        key, value = line.strip().split(" = ")
        nodes = value.strip("()").split(", ")
        graphs[key] = [node.strip() for node in nodes]

current_node = graphs["AAA"]
steps = 0

num_iters = 100000000
movement_cycle = itertools.cycle(movements)

for _ in range(num_iters):
    direction = next(movement_cycle)
    if direction == "R":
        current_node = graphs[current_node[1]]
        
    elif direction == "L":
        current_node = graphs[current_node[0]]
    
    steps += 1
    if current_node == graphs["ZZZ"]:
        break


print(current_node) 
print(steps)

