n = int(input())
adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)
num_edges = sum(row.count(1) for row in adj_matrix)
print(num_edges)