from random import Random
import time
# from threading import Barrier, Thread
import multiprocessing
from multiprocessing import Barrier
from multiprocessing.context import Process

mat_size = 200

random = Random()
process_count = 8


def generate_random_matrix(matrix):
    for row in range(mat_size):
        for col in range(mat_size):
            matrix[row*mat_size+col] = random.randint(-5, 5)


def work_out_row(id, matrix_a, matrix_b, result, work_start, work_complete):
    while True:
        work_start.wait()
        for row in range(id, mat_size, process_count):
            for col in range(mat_size):
                for i in range(mat_size):
                    result[row*mat_size+col] += matrix_a[row *
                                                         mat_size+i] * matrix_b[i*mat_size+col]

        work_complete.wait()


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    work_start = Barrier(process_count+1)
    work_complete = Barrier(process_count+1)

    matrix_a = multiprocessing.Array('i', [0]*mat_size*mat_size, lock=False)
    matrix_b = multiprocessing.Array('i', [0]*mat_size*mat_size, lock=False)
    result = multiprocessing.Array('i', [0]*mat_size*mat_size, lock=False)

    for p in range(process_count):
        Process(target=work_out_row, args=(
            [p, matrix_a, matrix_b, result, work_start, work_complete])).start()

    start = time.time()
    for i in range(19):
        generate_random_matrix(matrix_a)
        generate_random_matrix(matrix_b)

        for i in range(mat_size*mat_size):
            result[i] = 0

        work_start.wait()
        work_complete.wait()

    end = time.time()

    print(f"Done in {end-start}")
