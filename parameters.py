from sympy import isprime

# From Nitaj - useful values for N, p, q. 
# Yet to be implemented - q = 128,256 not valid parameters at this time.
#key_params = {"Low" : [11,3,61], "Moderate" : [167, 3, 128],
#              "Standard" : [251, 3, 128], "High" : [347,3,128],
#              "Highest" : [503, 3, 256]}

N, p, q = 503, 3, 257

df = 7
dg = 6
dr = 5

# Enforce constraints on NTRU Parameter set: 
assert df <= N
assert dg <= N
assert dr <= N

assert isprime(N)
assert isprime(p)
assert isprime(q)
