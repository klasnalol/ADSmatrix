from collections import deque
n = int(input())
adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)
start, end = map(int, input().split())
#find shortest path
visited = [False] * n
parent = [-1] * n
queue = deque()

queue.append(start - 1)
visited[start - 1] = True

while queue:
    current = queue.popleft()
    if current == end - 1:
        break

    for neighbor in range(n):
        if adj_matrix[current][neighbor] == 1 and not visited[neighbor]:
            visited[neighbor] = True
            parent[neighbor] = current
            queue.append(neighbor)
# the shortest path
path = []
if visited[end - 1]:
    node = end - 1
    while node != -1:
        path.append(node + 1)
        node = parent[node]
    path.reverse()
if visited[end - 1]:
    print(len(path) - 1)
    if path:
        print(*path)
else:
    print(-1)
