from prover import Prover
from verifier import Verifier
import time
import matplotlib.pyplot as plt
import math
import random
import authentication as auth
import utils

if __name__ == "__main__":

    print("\nAuthentication protocol test")

    p_values = []

    time_values = []

    k = 11

    while(len(p_values)<200):
        p = random.randint(pow(10,3),pow(10,4))
        if(utils.isPrime(p)):
            p_values.append(p)
    
    while(len(p_values)<400):
        p = random.randint(pow(10,4),pow(10,5)/2)
        if(utils.isPrime(p)):
            p_values.append(p)

    while(len(p_values)<600):
        p = random.randint(pow(10,5)/2,pow(10,5))
        if(utils.isPrime(p)):
            p_values.append(p)

    
    while(len(p_values)<800):
        p = random.randint(pow(10,5),pow(10,6)/4)
        if(utils.isPrime(p)):
            p_values.append(p)

    p_values.sort()

    for p in p_values:
        start_time = time.time()
        print("p: ", p)
        a = auth.generate_primitive(p)
        auth.authentication(p,a,k)
        end_time = time.time()
        time_values.append(end_time-start_time)
    
    plt.xlabel('p')
    plt.ylabel('time')
    plt.plot(p_values, time_values,'yo')
    plt.show()
