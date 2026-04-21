from collections import deque

# Input graph
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbours = input(f"Enter neighbours of {node} separated by space: ").split()
    graph[node] = neighbours

start = input("Enter starting node: ")


def bfs(graph, start):
    visited = []
    queue = deque()

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(graph, start)