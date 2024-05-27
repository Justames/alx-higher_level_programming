#!/usr/bin/python3

"function that computes square values of int in 2d a matrix"

def square_matrix_simple(matrix=[]):
    squared = []
    for row in matrix:
        squared_row = list(map(lambda x: x*x, row))
        squared.append(squared_row)
    return squared

