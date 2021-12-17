import numpy as np
import authentication as auth
from prover import Prover
from verifier import Verifier
import utils
import math
import matplotlib.pyplot as plt

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
    
    return (r_values)

def guess_key(attempts, iterations, p, k, r_list):

    i = 0

    success = 0


    print("Running ",iterations, " simulations...")

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

        if(math.gcd(t[0],p-1)==1):
            for r in r_list[-attempts:]:

                k_found = (B.c-r*t[1])*utils.modular_inverse(t[0],p-1)%(p-1)
                    
                if(k_found == k):
                    success +=1
                    break
        i+=1


    succ_prob = success/iterations
    print("Success probability: ",succ_prob, " (", round(succ_prob*100,2),"% )")
    return succ_prob



if __name__ == "__main__":

    p = 773
    k = 64
    print("\nChoosen variables: ")
    print(" p:", p)
    print(" k: ", k)
    print("\nGenerating the list of r values (from less probable to the most)...")

    r_list = find_best_r(p)

    print("[*] Success probability of a single masquerade attempt (checking only the most probable value of r)")
    
    guess_key(attempts=1, iterations=10000, p=p, k=k, r_list = r_list)

    print("\n[*] Success probability of n masquerade attempt")
    n_max = len(r_list)
    print(" Range n: 1 -", n_max)
    succ_probs = []
    n_list = list(range(1,n_max))
    for i in n_list:
        print("\nTest with ",i,"attempts...")
        succ_probs.append(guess_key(attempts=i, iterations=10000, p=p, k=k, r_list = r_list))
    plt.xlabel('attempts')
    plt.ylabel('success probability')
    plt.plot(n_list, succ_probs,'yo')
    plt.show()