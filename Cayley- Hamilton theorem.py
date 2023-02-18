import numpy as np
def is_diagonalizable(A):
    eigenvals, eigenvects = np.linalg.eig(A)
    if np.allclose(eigenvects.dot(np.diag(eigenvals)).dot(np.linalg.inv(eigenvects)), A):
        return True
    else:
        return False
def find_eigenvalues(A):
    eigenvals, _ = np.linalg.eig(A)
    return eigenvals
def verify_cayley_hamilton(A):
    n = A.shape[0]
    char_poly = np.poly(A)
    if np.allclose(np.dot(char_poly[:-1], A) + char_poly[-1]*np.eye(n), np.zeros((n,n))):
        return True
    else:
        return False
A = np.array([[1, 2, 3], [0, 4, 5], [0, 0, 6]])
print("Matrix A:\n", A)
if is_diagonalizable(A):
    print("Matrix A is diagonalizable.")
else:
    print("Matrix A is not diagonalizable.")
eigenvals = find_eigenvalues(A)
print("Eigenvalues of A:", eigenvals)
if verify_cayley_hamilton(A):
    print("Matrix A satisfies the Cayley-Hamilton theorem.")
else:
    print("Matrix A does not satisfy the Cayley-Hamilton theorem.")
