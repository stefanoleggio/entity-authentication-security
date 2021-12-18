import utils
from prover import Prover
from verifier import Verifier

if __name__ == "__main__":
    p =  3159553   
    alpha = 10     
    k_1 = 3082651

    c_a = 1323262  
    t_a = (610187, 1018690)

    c_b = 2511813  
    t_b = (610187 ,1684559)

    c_c = 126246

    # The r for t_a and t_b is the same:

    k = ((t_b[1]*c_a-t_a[1]*c_b)*utils.modular_inverse((t_a[0]*(t_b[1]-t_a[1])),p-1))%(p-1)

    print("key founded: ", k)
    print("Let's test the key ...")
    print("challenge: ", c_c)

    # Test k
    
    C = Prover(p,alpha,k)
    C.k_1 = k_1
    B = Verifier(p,alpha,C.k_1)
    B.c = c_c
    t = C.compute_tags(B.c)
    print("t: ",t)
    if(B.authenticate(t)):
        print("B authenticated C")
        print("C successfully masquerade A")
    else:
        print("B rejected C")    
