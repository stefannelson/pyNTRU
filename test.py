import numpy as np
from sympy.polys.domains import ZZ
from sympy.polys.galoistools import gf_gcdex
from ntru_utils import *


f = [-1,0,-1,0,-1,0,1,0,1,1,1]
N = 11
mod = 61

# Creates x^N - 1
xNminus1 = np.zeros(N+1)
xNminus1[0] = 1
xNminus1[-1] = -1

f_poly = ZZ.map(f)
x_mod = ZZ.map(xNminus1)
s, t, g = gf_gcdex(f_poly, x_mod, mod, ZZ)
if len(g) == 1 and g[0] == 1: 
    print(trunc_polynomial(s))
else:
    print('no inverse')

def find_inv(poly, mod):
    xNminus1 = np.zeros(N+1)
    xNminus1[0] = 1
    xNminus1[-1] = -1

    f_poly = ZZ.map(f)
    x_mod = ZZ.map(xNminus1)
    s, t, g = gf_gcdex(f_poly, x_mod, mod, ZZ)
    if len(g) == 1 and g[0] == 1:
        return trunc_polynomial(s)
    return trunc_polynomial(0)