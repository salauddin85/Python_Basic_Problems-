#  find gcd for 2 numbers

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
print(gcd(12,18))




