#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(lambda num: num ** 2, row)) for row in matrix]
    return new_matrix
