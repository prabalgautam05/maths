import numpy as np
v = np.array([1, 2, 3])
print("Original vector:", v)
v_t = v.T
print("Transpose vector:", v_t)
v_ct = v.conj().T
print("Conjugate transpose vector:", v_ct)
m = np.array([[1, 2, 3], [4, 5, 6]])
print("Original matrix:\n", m)
m_t = m.T
print("Transpose matrix:\n", m_t)
m_ct = m.conj().T
print("Conjugate transpose matrix:\n", m_ct)
