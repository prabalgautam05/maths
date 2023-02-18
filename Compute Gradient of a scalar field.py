import numpy as np

def gradient(f, x, y, z):
    dx = (f(x + 1e-6, y, z) - f(x, y, z)) / 1e-6
    dy = (f(x, y + 1e-6, z) - f(x, y, z)) / 1e-6
    dz = (f(x, y, z + 1e-6) - f(x, y, z)) / 1e-6
    return np.array([dx, dy, dz])

# example usage
def f(x, y, z):
    return x**2 + y**2 + z**2

x, y, z = 1, 2, 3
grad = gradient(f, x, y, z)
print("Gradient of f at (1, 2, 3):", grad)
