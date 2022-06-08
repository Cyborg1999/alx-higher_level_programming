#!/usr/bin/python3
def square_matrix_simple(matix = []):
    new_matrix = matix.copy()

    for i in range(len(matix)):
        new_matrix[i] = list(map(lambda x: x**2, matix[i]))
    
    return (new_matrix)