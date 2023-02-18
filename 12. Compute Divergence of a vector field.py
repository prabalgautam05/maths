import numpy as np

def divergence(u, v, w, x, y, z):
    du_dx = (u(x + 1e-6, y, z) - u(x, y, z)) / 1e-6
    dv_dy = (v(x, y + 1e-6, z) - v(x, y, z)) / 1e-6
    dw_dz = (w(x, y, z + 1e-6) - w(x, y, z)) / 1e-6
    return du_dx + dv_dy + dw_dz

# example usage
def u(x, y, z):
    return x**2 * y * z

def v(x, y, z):
    return x * y**2 * z

def w(x, y, z):
    return x * y * z**2

x, y, z = 1, 2, 3
div = divergence(u, v, w, x, y, z)
print("Divergence of (u, v, w) at (1, 2, 3):", div)
