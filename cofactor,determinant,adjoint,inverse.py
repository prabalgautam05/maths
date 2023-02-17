import numpy as np
A = np.array([[2, 3, 1],
              [4, 0, 2],
              [1, 2, 1]])
def cofactor(matrix, i, j):
    minor = np.delete(np.delete(matrix, i, 0), j, 1)
    return (-1) ** (i + j) * np.linalg.det(minor)
def cofactor_matrix(matrix):
    n = matrix.shape[0]
    cofactors = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            cofactors[i][j] = cofactor(matrix, i, j)
    return cofactors

# Find the cofactor matrix
C = cofactor_matrix(A)

# Find the determinant of the matrix
det = np.linalg.det(A)

adj = C.T
inv = adj / det
print("Matrix A:\n", A)
print("Cofactor matrix of A:\n", C)
print("Determinant of A:", det)
print("Adjoint of A:\n", adj)
print("Inverse of A:\n", inv)
