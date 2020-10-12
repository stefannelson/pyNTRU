from ntru_utils import *
from ntru_workflow import *
from parameters import *

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
