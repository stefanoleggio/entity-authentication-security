from prover import Prover
from verifier import Verifier

p = 11
a = 2

k = 4 # Private key of A


A = Prover(p,a,k)

B = Verifier(p,a,A.k_1)

B.generate_challenge()

t = A.compute_tags(B.c)

print("p: ", p)
print("a: ",a)
print("c: ", B.c)
if(B.authenticate(t)):
    print("A is authenticated by B")
else:
    print("A is rejected by B")