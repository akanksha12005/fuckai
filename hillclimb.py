import copy

def initial_state(n):
    return [list(range(n, 0, -1)), [], []]

def is_goal(state, n):
    return state[2] == list(range(n, 0, -1))

def heuristic(state):
    return len(state[2])

def generate_neighbors(state):
    neighbors = []

    for i in range(3):
        if not state[i]:
            continue

        for j in range(3):
            if i != j:
                if not state[j] or state[i][-1] < state[j][-1]:
                    new_state = copy.deepcopy(state)
                    disk = new_state[i].pop()
                    new_state[j].append(disk)
                    neighbors.append(new_state)

    return neighbors

def hill_climbing(n):
    current = initial_state(n)
    visited = []
    step = 0

    print("Initial State:", current)

    while not is_goal(current, n):
        visited.append(current)
        neighbors = generate_neighbors(current)

        best_neighbor = None
        best_h = -1

        for neighbor in neighbors:
            if neighbor not in visited:
                h = heuristic(neighbor)

                if h >= best_h:
                    best_h = h
                    best_neighbor = neighbor

        if best_neighbor is None:
            print("Stuck at Local Optimum")
            return

        current = best_neighbor
        step += 1
        print(f"Step {step}: {current} Heuristic = {best_h}")

    print("\nGoal Reached!")

n = 3
hill_climbing(n)