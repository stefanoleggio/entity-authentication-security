from prover import Prover
from verifier import Verifier
import authentication as auth

if __name__ == "__main__":

    p = 1702079

    k = 2 # This key is randomly choosen (is not the correct key for the k_1 given) just for initialize the Prover object

    k_1 = 7

    alpha = 948347

    C = Prover(p,alpha,k)

    C.k_1 = k_1

    B = Verifier(p,alpha,C.k_1)

    B.c = 732904

    print("\nChoosen variables: ")
    print(" p:", p)
    print(" k_1: ", k_1)
    print(" alpha:",alpha)
    print(" c:", B.c)

    C.compute_tags_v2(B.c)

    t_1_prime = C.k_1 %p

    t_2_prime = -t_1_prime % (p-1)

    n = (-B.c)%p

    t = (n,t_1_prime,t_2_prime)

    if(B.authenticate_v2(t)):
        print("B authenticated C")
        print("C successfully masquerade A")
    else:
        print(" C is rejected by B")