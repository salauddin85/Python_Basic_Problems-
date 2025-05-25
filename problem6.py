# 6. Find the sum of all numbers in a list
# Input: [1, 2, 3, 4]
#  Output: 10

def find_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
# Test the function
print(find_sum([1, 2, 3, 4]))  # Output: 10