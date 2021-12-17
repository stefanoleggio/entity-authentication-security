import random
import utils
import math 

class Prover:

    def __init__(self, p, alpha, k):
        self.p = p
        self.alpha = alpha
        self.k = k # Private key
        self.k_1 = pow(self.alpha,self.k)%self.p # Public key

    def compute_tags(self,c):
        while(True):
            r_1 = random.randint(0, self.p)
            digits = str(r_1)
            r = 0    
            for digit in digits:
                r += int(digit)
            if(math.gcd(r,(self.p-1)) == 1):
                break
        self.r = r

        t_1 = pow(self.alpha,r) % self.p
        t_2 = (c-self.k*t_1) * utils.modular_inverse(r,self.p-1) % (self.p-1)

        return (t_1, t_2)

    
    def compute_tags_v2(self,c):
        n = random.randint(0,self.p)
        self.n = n
        u = (c + n)%self.p
        while(True):
            r_1 = random.randint(0, self.p)
            digits = str(r_1)
            r = 0    
            for digit in digits:
                r += int(digit)
            if(math.gcd(r,(self.p-1)) == 1):
                break
        self.r = r
        self.u = u
        t_1 = pow(self.alpha,r) % self.p
        t_2 = (u-self.k*t_1) * utils.modular_inverse(r,self.p-1) % (self.p-1)

        return (u, t_1, t_2)