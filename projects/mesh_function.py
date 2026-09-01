from collections.abc import Callable

import numpy as np


def mesh_function(f: Callable[[float], float], t: np.ndarray) -> np.ndarray:
    f_arr = np.zeros(len(t))
    for i, t_i in enumerate(t):
        f_arr[i] = f(t_i)
    return f_arr

def func(t: float) -> float:
    if 0 <= t and t <= 3:
        f = np.exp(-t)
    elif 3 < t and t <= 4:
        f = np.exp(-3*t)
    return f

def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)

if __name__ == "__main__":
    test_mesh_function()
