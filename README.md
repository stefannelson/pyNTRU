# pyNTRU

Simple Python implementation of NTRU. This implementation is still an early build and **not** suitable for cybersecurity applications. 

# Execution

While in this directory, run the following command:

```>> python main.py```

This will output a polynomial message (string -> polynomial functionality will be added in a later release), the encrypted ciphertext, and the decrypted original message. Note that the encryption is based on random selection of polynomials, so the output will likely change on repeated runs. 