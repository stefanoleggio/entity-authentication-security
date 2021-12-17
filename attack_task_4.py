from prover import Prover
from verifier import Verifier
import authentication as auth
import random

if __name__ == "__main__":
    p = 11
    k = 4
    alpha = auth.generate_primitive(p)
    A = Prover(p,alpha,k)
    B = Verifier(p,alpha,A.k_1)
    B.generate_challenge()
    t = A.compute_tags_v2(B.c)

    if(B.authenticate_v2(t)):
        print(" A is authenticated by B")
    else:
        print(" A is rejected by B")

    q = random.randint(0,p-1)

    t_1_prime = A.k_1 * pow(alpha,q) %p
    t_2_prime = -t_1_prime % (p-1)
    t = (A.u,t_1_prime,t_2_prime)
    print(B.authenticate_v2(t))
