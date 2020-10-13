from ntru_utils import *
from ntru_workflow import *
from parameters import *

# Input message (np.array or list)
# ! Polynomial must be in Z_p[X]/(X^n - 1)
# ! whose coefficients are between +- p/2
# e.g. coefficients can be +- 1, +- 2, 0 for p=3
message = [1,0,1,1,-1,0,1]

# Test Key Generation
pub_key, pri_key = keyGen(p,q,N)

# Output message as polynomial 
print(trunc_polynomial(message))

# Encrypt and output
ciphertext = encrypt(message, pub_key)
print(ciphertext)

# Decrypt, output, and determine if it's same as original msg
new_message = decrypt(ciphertext, pri_key)
print(new_message)
print(trunc_polynomial(message).mod(p) == new_message)
'''

ftest = trunc_polynomial([-1,-1,1,-1,1,0,-1,1,0,0])
fqtest = trunc_polynomial([31,12,46,42,56,46,49,2,22,46,5])
fqtest = trunc_polynomial([31,12,46,42,60,50,49,2,22,46,5])


print(ftest); print()
print(fqtest)

print(ftest.convolution(fqtest).mod(61) == trunc_polynomial(1))
'''