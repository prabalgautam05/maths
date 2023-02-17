import numpy as np
A = np.array([[2, -3, 1],
              [-1, 2, 1],
              [1, 1, 5]])
I = np.eye(len(A))

A_aug = np.column_stack((A, I))
for i in range(len(A)):
    max_row = i
    for j in range(i+1, len(A)):
        if abs(A_aug[j][i]) > abs(A_aug[max_row][i]):
            max_row = j
    A_aug[[i, max_row]] = A_aug[[max_row, i]]
    pivot = A_aug[i][i]
    A_aug[i] /= pivot
    for j in range(len(A)):
        if j != i:
            factor = A_aug[j][i]
            A_aug[j] -= factor * A_aug[i]
X = A_aug[:, len(A):]
print("Solution: ", X)
