n = int(input())
adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)
degrees = [sum(row) for row in adj_matrix]
for degree in degrees:
    print(degree)
