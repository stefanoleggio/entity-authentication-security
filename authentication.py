from prover import Prover
from verifier import Verifier
import matplotlib.pyplot as plt
import random

def generate_primitive(p):
    a = random.randint(0, p)
    return a

def authentication(p,a,k):
    A = Prover(p,a,k)
    B = Verifier(p,a,A.k_1)
    B.generate_challenge()
    t = A.compute_tags(B.c)
    return B.authenticate(t)

if __name__ == "__main__":

    print("\nAuthentication protocol test")

    p = 11
    alpha = generate_primitive(p)
    k = 4 # Private key of A

    A = Prover(p,alpha,k)

    B = Verifier(p,alpha,A.k_1) # In this case B knows the public key of A

    B.generate_challenge()

    t = A.compute_tags(B.c)
    print("\nSetup variables")
    print(" p: ", p)
    print(" a: ",alpha)
    print(" c: ", B.c)
    print("\nKeys of A")
    print(" k: ", k, "(private key)")
    print(" k_1: ", A.k_1, "(public key)")
    print("\nResult: ")
    if(B.authenticate(t)):
        print(" A is authenticated by B")
    else:
        print(" A is rejected by B")
