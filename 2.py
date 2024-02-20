n = int(input())
adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)
#self-loops
has_loop = any(adj_matrix[i][i] != 0 for i in range(n))
if has_loop:
    print("YES")
else:
    print("NO")