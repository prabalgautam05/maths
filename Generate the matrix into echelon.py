import numpy as np
M = np.random.rand(4, 5)
print("Original matrix:\n", M)
for i in range(M.shape[1]):
    pivot = np.argmax(np.abs(M[i:, i])) + i
    if pivot != i:
        M[[i, pivot]] = M[[pivot, i]]
    for j in range(i+1, M.shape[0]):
        factor = M[j, i] / M[i, i]
        M[j, i:] -= factor * M[i, i:]
print("Matrix in echelon form:\n", M)
rank = np.sum(np.abs(np.diag(M)) > 1e-6)
print("Rank of the matrix:", rank)
