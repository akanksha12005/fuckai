import heapq

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# Heuristic function
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

# Find blank
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Moves
def moves(state):
    x, y = find_blank(state)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    children = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            children.append(new_state)

    return children

# A* Search
def a_star(start):
    pq = []
    count = 0  # tie-breaker

    heapq.heappush(pq, (heuristic(start), 0, count, start, []))
    visited = set()

    while pq:
        f, g, _, state, path = heapq.heappop(pq)

        if state == goal:
            return path + [state]

        visited.add(tuple(map(tuple, state)))

        for child in moves(state):
            child_tuple = tuple(map(tuple, child))

            if child_tuple not in visited:
                count += 1
                new_g = g + 1
                new_f = new_g + heuristic(child)

                heapq.heappush(pq, (new_f, new_g, count, child, path + [state]))

    return None

# Input
start = []
print("Enter initial state row by row (use 0 for blank):")

for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)

solution = a_star(start)

if solution:
    print("\nSolution Steps:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")
OUTPUT:
1 2 3
4 0 6 
7 5 8