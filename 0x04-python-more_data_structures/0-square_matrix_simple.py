#!/usr/bin/python3


# Define a func that calculates the sqr value of all integers of a matrix
def square_matrix_simple(matrix=[]):
    return list(map(lambda submat: list(map(lambda e: e**2, submat)), matrix))
