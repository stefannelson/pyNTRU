from ntru_utils import *
from ntru_workflow import *
from parameters import *

'''
# Test Finding Inverse of f. 

modulus = q

test = np.array([-1,0,-1,0,-1,0,1,0,1,1,1]) #% f
test_poly = trunc_polynomial(test)

ans = find_inv(test, modulus)
ans_poly = trunc_polynomial(ans)
# ans_poly = trunc_polynomial([1,0,1,0,1,2,2,2,1,0])  # Ans for fp
# ans_poly = trunc_polynomial([45,49,26,40,53,47,21,24,60,32,31]) # Ans for fq

# print(test_poly)
print(trunc_polynomial(test_poly.c % modulus), '\n')
print(ans_poly, '\n')
print(test_poly.convolution(ans_poly).c % modulus)
'''

# Test Key Generation, Encryption, Decryption

pub_key, pri_key = keyGen(p,q,N)

print(trunc_polynomial(message))

ciphertext = encrypt(message, pub_key)
print(ciphertext)


new_message = decrypt(ciphertext, pri_key)
print(new_message)
print(trunc_polynomial(message).mod(p) == new_message)
