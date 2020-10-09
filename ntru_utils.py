import numpy as np
from random import SystemRandom
from sympy import symbols, div, Poly
from parameters import *


class trunc_polynomial(np.poly1d):
    '''
    Create child class of numpy's poly1d class. 
    Preserves element-wise addition, subtraction, etc.
    but adds in convolution and modular arithmetic to ensure 
    element is in ring Z_q = Z/qZ.
    '''

    def scale(self, mod, center = False):
        '''
        Adjusts coefficients of a polynomial to be within a 
        certain bound defined by mod. The 'center' flag
        specifies when coefficients must be within +- mod.
        '''
        for i in range(len(self)+1):
            if center:
                if self[i] < -mod:
                    self[i] += int(mod*2)
                elif self[i] > mod:
                    self[i] -= int(mod*2)
            elif center == False and self[i] < 0:
                self[i] += mod 
        return self

    def convolution(self, other):
        '''
        Multiplication in truncated polynomial rings. If 
        an exponent is after typical polynomial multiplication
        is greater than N, the corresponding coefficient is 
        added to the exponent mod N. 
        '''
        result = trunc_polynomial(np.zeros(N))
        
        init_prod = self*other
        
        for ct in range(len(init_prod)+1):
            if ct < N: 
                result[ct] += init_prod[ct]
            else:
                result[ct % N] += init_prod[ct]
 
        return result

    def mod(self, modulus):
        '''
        Efficiently takes every coefficient and 
        calculates the coeffcient mod p/q. 
        '''
        return trunc_polynomial( self.c % modulus )

    
def B(d):
    '''
    Randomly picks from a binary set of polynomials of degree N with d ones and N-d zeros. 

    Example: 
    --------
    B(5)

    > 
        7     5     4     3
    -1 x + 1 x + 1 x + 1 x + 1 x
    '''
    polynomial = np.zeros(N)
    sr = SystemRandom()
    while np.count_nonzero(polynomial == 1) + np.count_nonzero(polynomial == -1) < d:
        polynomial[ sr.choice(np.where(polynomial == 0)[0]) ] += sr.choice([-1,1])
    return trunc_polynomial(polynomial)


def poly_div_mod(num, den, mod):
    '''
    Divides polynomials under a certain modulus utilizing sympy. 
    '''
    x = symbols('x')
    num = Poly(num, x, modulus = mod)
    den = Poly(den, x, modulus = mod)
    
    quo = div(num, den, modulus = mod)
    return [np.array(quo[0].all_coeffs()) % mod, 
            np.array(quo[1].all_coeffs()) % mod]

def eea(a,b):
    '''
    Finds gcd(a,b) with s,t such that as + bt = gcd(a,b)
    utilizing the extended euclidean algorithm (iterative)
    '''
    if a < b: 
        a,b = b,a

    i = 1
    R = [a,b]
    Q = [0]
    
    # Find GCD(a,b) - keep q_i, r_i's
    Q.append(a // b)
    R.append(a % b)
    while R[-1] != 0:
        Q.append( R[i] // R[i+1] )
        R.append( R[i] % R[i+1] )
        i += 1
    i_max = i

    # Extended Euclidean
    i = 2
    S = [1,0]
    T = [0,1]
    while i <= i_max:
        S.append(S[i-2] - (Q[i-1]*S[i-1]))
        T.append(T[i-2] - (Q[i-1]*T[i-1]))
        i += 1
    
    gcd = R[-2]
    s = S[-1]
    t = T[-1]

    return gcd, s, t

def find_inv(poly, mod): 
    '''
    Takes a function f and finds a polynomial that 
    is its inverse mod p/q. 

    Inputs:
    -------
    poly : np.array
    mod  : int
    '''

    xNminus1 = np.zeros(N+1)
    xNminus1[0] = 1                                 # Creates x^N - 1
    xNminus1[-1] = -1

    xNminus1 = (xNminus1 % mod).astype(int)
    poly = (poly.c % mod).astype(int)
    

    tmp = poly_div_mod(poly, xNminus1, mod)
    r = [poly, xNminus1, tmp[1]]
    q = [np.array([0]), np.array([0]), tmp[0]]
    i = 2

    while len(r[i]) > 1 and r[i][0] != 0: 
        i += 1

        tmp = poly_div_mod(r[i-2], r[i-1], mod)

        q.append(tmp[0])
        r.append(tmp[1])
    i_max = i

    '''
    print('q:')
    for ind in q:
        print(trunc_polynomial(ind))
    
    print("r:")
    for ind in r:
        print(trunc_polynomial(ind))
    '''

    i = 2
    A = [trunc_polynomial(1), trunc_polynomial(0)]
    B = [trunc_polynomial(0), trunc_polynomial(1)]
    while i <= i_max:
        A.append(A[i-2] - (trunc_polynomial(q[i])*A[i-1]))
        B.append(B[i-2] - (trunc_polynomial(q[i])*B[i-1]))
        i += 1
    
    inv = 1
    if r[-1] != 0:
        inv = eea(r[-1], mod)[-1]

    return trunc_polynomial((inv*A[-1].coeffs) % mod)