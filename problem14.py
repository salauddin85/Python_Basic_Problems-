# check the any number is prime or not without any builtin function

def is_prime(num):
    if num <= 1:
        return False
    
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i = i + 1
    
    return True

# test
print(is_prime(2))  # True
print(is_prime(4))  # False
print(is_prime(17)) # True
print(is_prime(100))# False
