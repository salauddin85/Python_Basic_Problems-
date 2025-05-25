# ৯. find out the factorial 
# Input: 5
#  Output: 120

def factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    if n == 0 or n == 1:
        return 1  # Base case: factorial of 0 and 1 is 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
# Test the function
print(factorial(5))  # Output: 120
