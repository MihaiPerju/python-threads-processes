

matrix_a = [
    [3,  1, -4],
    [2, -3,  1],
    [5, -2,  0]
]

matrix_b = [
    [ 1,  -2, -1],
    [ 0,   5,  4],
    [-1,  -2,  3]
]
mat_size = len(matrix_a)
result = [[0]*mat_size for _ in range(mat_size)]

for row in range(mat_size):
    for col in range(mat_size):
        for i in range(mat_size):
            result[row][col] += matrix_a[row][i] * matrix_b[i][col]

for row in range(mat_size):
    mat_row = ""
    for col in range(mat_size):
        mat_row += str(result[row][col])+" "
    print(mat_row)
