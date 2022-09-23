#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if x != 0:
                print(" ", end="")
            print("{:d}".format(matrix[y][x]), end="")
        print()
