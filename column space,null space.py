import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
col_space_basis = np.linalg.matrix_rank(A)
print("Column space basis: ", col_space_basis)
null_space_basis = np.linalg.null_space(A)
print("Null space basis: ")
print(null_space_basis)
row_space_basis = np.linalg.matrix_rank(A.T)
print("Row space basis: ", row_space_basis)
left_null_space_basis = np.linalg.null_space(A.T)
print("Left null space basis: ")
print(left_null_space_basis)
