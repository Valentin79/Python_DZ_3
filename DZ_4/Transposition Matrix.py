# Напишите функцию для транспонирования матрицы

import numpy

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)


def easy_transpose_matrix(m):
    return numpy.transpose(m)


def transpose_matrix(matrix):
    res = []
    n = len(matrix)
    m = len(matrix[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [matrix[i][j]]
        res = res + [tmp]
    return res


print(easy_transpose_matrix(matrix))
print(transpose_matrix(matrix))
for line in transpose_matrix(matrix):
    print(line)
