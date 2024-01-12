
#? Write a Python function gcd to return the greatest common divisor (GCD) of two positive integer parameters
# print(gcd(24,36))

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a
