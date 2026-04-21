MAX = 20
INF = 9999

graph = [[INF for _ in range(MAX)] for _ in range(MAX)]
visited = [0] * MAX
parent = [-1] * MAX
cost = [INF] * MAX

# Initialize graph
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

print("Enter edges (from to cost):")
for _ in range(e):
    u, v, c = map(int, input().split())
    graph[u][v] = c

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))

# Initialize cost and parent
for i in range(n):
    cost[i] = INF
    parent[i] = -1
    visited[i] = 0

cost[start] = 0
nodes_visited = 0

while True:
    min_cost = INF
    u = -1

    # Find minimum cost node
    for i in range(n):
        if not visited[i] and cost[i] < min_cost:
            min_cost = cost[i]
            u = i

    if u == -1:
        break

    visited[u] = 1
    nodes_visited += 1

    if u == goal:
        break

    # Update neighbors
    for v in range(n):
        if not visited[v] and graph[u][v] != INF:
            if cost[u] + graph[u][v] < cost[v]:
                cost[v] = cost[u] + graph[u][v]
                parent[v] = u

if not visited[goal]:
    print("Goal not reachable")
else:
    # Print path in reverse
    print("Path:", end=" ")
    cur = goal
    while cur != -1:
        print(cur, end=" ")
        cur = parent[cur]

    print("\nTotal cost:", cost[goal])
    print("Nodes visited:", nodes_visited)



