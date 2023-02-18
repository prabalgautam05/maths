import numpy as np
def gram_schmidt(vectors):
    n = len(vectors)
    q = np.zeros((n, n))
    for i in range(n):
        q[i] = vectors[i]
        for j in range(i):
            q[i] -= np.dot(vectors[i], q[j]) / np.dot(q[j], q[j]) * q[j]
        q[i] /= np.linalg.norm(q[i])
    return q
vectors = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])]
q = gram_schmidt(vectors)
print(q)
