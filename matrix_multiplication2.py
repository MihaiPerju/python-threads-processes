from random import Random
import time
mat_size = 200

random = Random()

start = time.time()
for i in range(19):
    matrix_a = [[0]*mat_size for _ in range(mat_size)]
    matrix_b = [[0]*mat_size for _ in range(mat_size)]
    result = [[0]*mat_size for _ in range(mat_size)]

    for row in range(mat_size):
        for col in range(mat_size):
            matrix_a[row][col] = random.randint(-5, 5)
            matrix_b[row][col] = random.randint(-5, 5)


    for row in range(mat_size):
        for col in range(mat_size):
            for i in range(mat_size):
                result[row][col] += matrix_a[row][i] * matrix_b[i][col]
end = time.time()

print(f"Done in {end-start}")
