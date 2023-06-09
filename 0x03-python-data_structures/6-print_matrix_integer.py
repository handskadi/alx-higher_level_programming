#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # a func that print a matrix of int
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][j]), end='')
        print()
