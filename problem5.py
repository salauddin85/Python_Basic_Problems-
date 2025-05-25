# Don't code suggestions using AI tools
# Problem 5. Find the minimum number in a list
# Input: [2, 5, 1, 9, 7]
#  Output: 1

def find_minimum(numbers):
    if not numbers:
        return None  # Handle empty list case
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num
# Test the function
print(find_minimum([2, 5, 1, 9, 7]))  # Output: 1