N, S = map(int, input().split())
adj_matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    adj_matrix.append(row)
#visited array
visited = [False] * N
# Depth-first search
stack = [S - 1]  # Subtract 1 from S to match 0-based indexing
visited[S - 1] = True  # Mark the starting vertex as visited
count = 1  # Counting the current vertex
while stack:
    vertex = stack.pop()
    for i in range(N):
        if adj_matrix[vertex][i] == 1 and not visited[i]:
            stack.append(i)
            visited[i] = True
            count += 1
print(count)