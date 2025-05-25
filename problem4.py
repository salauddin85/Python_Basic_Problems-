# Problem 4. Find the maximum number in a list
# Input: [2, 5, 1, 9, 7]
#  Output: 9

def find_maximum(numbers):
    if not numbers:
        return None  # Handle empty list case
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
# Test the function
print(find_maximum([2, 5, 1, 9, 7]))  # Output: 9