# Use sympy for prime number generation
from sympy import randprime
from math import gcd

def generate_keys():
    p, q = randprime(100, 300), randprime(100, 300)
    n = p * q
    phi = (p-1)*(q-1)
    e = 65537
    while gcd(e, phi) != 1:
        e += 2
    d = pow(e, -1, phi)
    return ((e, n), (d, n))

def encrypt(msg, pubkey):
    e, n = pubkey
    return [pow(ord(c), e, n) for c in msg]

def decrypt(cipher, privkey):
    d, n = privkey
    return ''.join([chr(pow(c, d, n)) for c in cipher])
