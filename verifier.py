import random

class Verifier:

    def __init__(self, p, a, k_1):
        self.p = p
        self.a = a
        self.c = None
        self.k_1 = k_1 # In this case the verifier knows the public key of the Prover
    
    def generate_challenge(self):
        self.c = random.randint(0, self.p-1)
        return self.c

    def authenticate(self, t):
        s = pow(self.a,self.c) % self.p
        s_tilda = pow(self.k_1, t[0]) * pow(t[0],t[1]) % (self.p)
        if(s == s_tilda):
            return True
        return False