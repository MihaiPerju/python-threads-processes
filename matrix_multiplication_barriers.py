from random import Random
import time
from threading import Barrier, Thread


mat_size = 200

matrix_a = [[0]*mat_size for _ in range(mat_size)]
matrix_b = [[0]*mat_size for _ in range(mat_size)]
result = [[0]*mat_size for _ in range(mat_size)]

random = Random()

work_start = Barrier(mat_size+1)
work_complete = Barrier(mat_size+1)

def generate_random_matrix(matrix):
    for row in range(mat_size):
        for col in range(mat_size):
            matrix[row][col] = random.randint(-5, 5)


def work_out_row(row):
    while True:
        work_start.wait()
        for col in range(mat_size):
            for i in range(mat_size):
                result[row][col] += matrix_a[row][i] * matrix_b[i][col]

        work_complete.wait()


for row in range(mat_size):
    Thread(target=work_out_row, args=([row])).start()

start = time.time()
for i in range(19):
    generate_random_matrix(matrix_a)
    generate_random_matrix(matrix_b)
    result = [[0]*mat_size for _ in range(mat_size)]

    work_start.wait()
    work_complete.wait()

end = time.time()

print(f"Done in {end-start}")
