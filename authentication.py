from prover import Prover
from verifier import Verifier
import time
import numpy as np
import random
import matplotlib.pyplot as plt
import math

def generate_primitive(p):
    while(True):
        a = random.randint(0, p)
        if(math.gcd(p,a) == 1):
            break
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
    a = generate_primitive(p)
    k = 4 # Private key of A

    A = Prover(p,a,k)

    B = Verifier(p,a,A.k_1) # In this case B knows the public key of A

    B.generate_challenge()

    t = A.compute_tags(B.c)
    print("\nSetup variables")
    print(" p: ", p)
    print(" a: ",a)
    print(" c: ", B.c)
    print("\nKeys of A")
    print(" k: ", k, "(private key)")
    print(" k_1: ", A.k_1, "(public key)")
    print("\nResult: ")
    if(B.authenticate(t)):
        print(" A is authenticated by B")
    else:
        print(" A is rejected by B")

    p_values = [1187,2707,4339,6073,7841,11527,17291,21211,70241,104147,162881,206413,449399,663517,993793]
    time_values = []

    for p in p_values:
        start_time = time.time()
        a = generate_primitive(p)
        authentication(p,a,k)
        end_time = time.time()
        time_values.append(end_time-start_time)

    plt.xlabel('p')
    plt.ylabel('time')
    plt.plot(p_values, time_values,'yo')
    plt.show()

