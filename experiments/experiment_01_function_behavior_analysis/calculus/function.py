import numpy as np
import sympy as sp

def f(x):
    #Experimental function (function for testing purposes)

    # --- floor(x) ---
    # if isinstance(x, sp.Basic):
    #     return sp.floor(x)
    # return np.floor(x)

    # --- original ---
    return x**3 - 3*x**2 + 2