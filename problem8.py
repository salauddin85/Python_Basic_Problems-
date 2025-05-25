#  problem8 - Remove duplicates from a list while without builtin functions
# Input: [1, 2, 2, 3, 1, 4]
#  Output: [1, 2, 3, 4]

def remove_duplicates(numbers):
    unique_num = []
    for num in numbers:
        if num not in unique_num:
            unique_num+= [num]
    return unique_num
    
# # Test the function
print(remove_duplicates([1, 2, 2, 3, 1, 4]))  # Output: [1, 2, 3, 4]

 # Output: [1, 2, 3, 4]