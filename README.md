# pyNTRU

Simple Python implementation of NTRU. This implementation is still an early build and **not** suitable for cybersecurity applications. 

# Execution

While in this directory, run the following command:

```>> python main.py```

This will output a polynomial message (string -> polynomial functionality will be added in a later release), the encrypted ciphertext, and the decrypted original message. Note that the encryption is based on random selection of polynomials, so the output will likely change on repeated runs. 

# Content
This repository contains the following files: 

1. `parameters.py` stores NTRU parameters N, p, q, d_f, d_g, d_r.
2. `ntru_utils.py` implements helper functions and the truncated polynomial class. 
3. `ntru_workflow.py` contains individual functions for key generation, encryption, and decryption.
4. `main.py` includes a test to encrypt and decrypt a message m. 

# Dependencies
This repository relies on the `numpy` and `sympy` packages for polynomial and modular polynomial division operations.

# Author
* Stefan Nelson (swn34@nau.edu)