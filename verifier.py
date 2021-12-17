import random

class Verifier:

    def __init__(self, p, alpha, k_1):
        self.p = p
        self.alpha = alpha
        self.c = None
        self.k_1 = k_1 # the verifier knows the public key of the Prover
    
    def generate_challenge(self):
        self.c = random.randint(0, self.p-1)
        return self.c

    def authenticate(self, t):
        s = pow(self.alpha,self.c) % self.p
        s_tilda = pow(self.k_1, t[0]) * pow(t[0],t[1]) % (self.p)
        if(s == s_tilda):
            return True
        return False

    def authenticate_v2(self, t):
        u = (self.c + t[0])%self.p
        s = pow(self.alpha,u) % self.p
        s_tilda = pow(self.k_1, t[1]) * pow(t[1],t[2]) % (self.p)
        if(s == s_tilda):
            return True
        return False