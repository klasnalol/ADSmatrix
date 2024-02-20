n = int(input())
adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)
# symmetry
symmetric = True
for i in range(n):
    for j in range(i+1, n):
        if adj_matrix[i][j] != adj_matrix[j][i]:
            symmetric = False
            break
    if not symmetric:
        break
#self-loops (diagonal elements)
self_loops = all(adj_matrix[i][i] == 0 for i in range(n))
if symmetric and self_loops:
    print("YES")
else:
    print("NO")

