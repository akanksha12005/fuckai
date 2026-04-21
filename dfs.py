# Input graph
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbours = input(f"Enter neighbours of {node} separated by space: ").split()
    graph[node] = neighbours

start = input("Enter starting node: ")

visited = []


def dfs(node):
    if node not in visited:
        visited.append(node)
        print(node, end=" ")

        for neighbour in graph[node]:
            dfs(neighbour)


dfs(start)