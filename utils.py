def modular_inverse(a, m):
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        raise Exception('The modular inverse does not exist.')

    while (a > 1):

        q = a // m

        t = m

        m = a % m
        a = t
        t = y

        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0

    return x

def isPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False
    return True