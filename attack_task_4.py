from prover import Prover
from verifier import Verifier
import authentication as auth
import random

if __name__ == "__main__":

    p = 1702079

    k = 7

    alpha = 948347

    C = Prover(p,alpha,k)

    B = Verifier(p,alpha,C.k_1)

    B.c = 732904

    print("\nChoosen variables: ")
    print(" p:", p)
    print(" k: ", k)
    print(" alpha:",alpha)
    print(" c:", B.c)

    C.compute_tags_v2(B.c)

    t_1_prime = C.k_1 %p

    t_2_prime = -t_1_prime % (p-1)
    print("\n")
    print("t_1_prime:",t_1_prime)
    print("t_2_prime:",t_2_prime)
    print("\n")

    n = (-B.c)%p

    t = (n,t_1_prime,t_2_prime)

    if(B.authenticate_v2(t)):
        print("B authenticated C")
        print("C successfully masquerade A")
    else:
        print(" C is rejected by B")