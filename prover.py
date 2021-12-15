import random
import utils
import math 

class Prover:

    def __init__(self, p, a, k):
        self.p = p
        self.a = a
        self.k = k # Private key
        self.k_1 = pow(self.a,self.k)%self.p # Public key

    def compute_tags(self,c):
        while(True):
            r_1 = random.uniform(0, self.p-1)
            digits = str(r_1)[2::]
            r = 0    
            for digit in digits:
                r += int(digit)
            if(math.gcd(r,(self.p-1)) == 1):
                break
            
        t_1 = pow(self.a,r) % self.p
        t_2 = round((c-self.k*t_1) * utils.modular_inverse(r,self.p-1))% (self.p-1)

        return (t_1, t_2)