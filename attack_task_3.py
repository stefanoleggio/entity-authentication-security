import numpy as np
import authentication as auth
from prover import Prover
from verifier import Verifier
import utils
import math

def find_best_r(p):
    r_prob = []
    r_values = []
    for r_1 in range(0,p+1):
        r = 0
        for digit in str(r_1):
            r += int(digit)

        found = False
        for i in range(len(r_values)):
            if(r_values[i] == r):
                r_prob[i] += 1
                found = True
        if(found == False):
            r_values.append(r)
            r_prob.append(1)

    # Reorder list

    r_prob,r_values = list(zip(*sorted(zip(r_prob, r_values))))

    print(r_values)
    
    return (r_values)

def guess_key(attempts, iterations,p,k):

    print("Guessing the value of k observing only one round")

    i = 0

    success = 0

    print("Running ",iterations, " simulations...")

    r_list = find_best_r(p)


    while(i<iterations):

        # Setup parameters

        alpha = auth.generate_primitive(p)
        
        # Observing the run of the protocol

        A = Prover(p,alpha,k)
        B = Verifier(p,alpha,A.k_1)
        B.generate_challenge()
        t = A.compute_tags(B.c)
        B.authenticate(t)

        # End run

        keyfounded = False

        for r in r_list[-attempts:]:

            k_found = (B.c-r*t[1])*utils.modular_inverse(t[0],p)%(p)

            if(k_found == k):
                success +=1
                keyfounded = True
                break
        
        if(keyfounded == False):
            print("r: ", A.r)
            print("alpha: ", A.alpha)
            print("t: ", t)
            print("p: ", p)
            print("k: ", k)
            k_found = (B.c-r*t[1])*utils.modular_inverse(t[0],p)%(p)
            print("k_found: ", k_found)

        i+=1


    succ_prob = success/iterations
    print("Success probability: ",succ_prob)


if __name__ == "__main__":

    guess_key(1, 1,503,3)