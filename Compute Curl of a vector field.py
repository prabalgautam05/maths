import numpy as np

def curl(u, v, w, x, y, z):
    du_dy = (u(x, y + 1e-6, z) - u(x, y, z)) / 1e-6
    du_dz = (u(x, y, z + 1e-6) - u(x, y, z)) / 1e-6
    dv_dx = (v(x + 1e-6, y, z) - v(x, y, z)) / 1e-6
    dv_dz = (v(x, y, z + 1e-6) - v(x, y, z)) / 1e-6
    dw_dx = (w(x + 1e-6, y, z) - w(x, y, z)) / 1e-6
    dw_dy = (w(x, y + 1e-6, z) - w(x, y, z)) / 1e-6
    return np.array([dw_dy - dv_dz, du_dz - dw_dx, dv_dx - du_dy])

# example usage
def u(x, y, z):
    return x**2 * y * z

def v(x, y, z):
    return x * y**2 * z

def w(x, y, z):
    return x * y * z**2

x, y, z = 1, 2, 3
curl_vec = curl(u, v, w, x, y, z)
print("Curl of (u, v, w) at (1, 2, 3):", curl_vec)
