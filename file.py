n = int(input())
m = int(input())

matrix = []
matrix_with_max = []
matrix_with_max_output = []
for i in range(n):
    sk = []
    for j in range(m):
        sk.append([0])
    matrix.append(sk)

for p in range(n):
    matrix[p] = input().split(" ")

for a in range(n):
    maximum_str = []
    maximum_int = []
    for c in range(m):
        maximum_str.append(matrix[a][c])
    for z in maximum_str:
        maximum_int.append(int(z))
    matrix_with_max.append(max(maximum_int))

for h in range(n):
    for s in range(m):
        if int(matrix[h][s]) == max(matrix_with_max):
            matrix_with_max_output.append((h, s))

print(*min(matrix_with_max_output))