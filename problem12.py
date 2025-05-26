# How many odd numbers in the List count it
# input : [2,10,11,56,98,23,22]
# output: 2

def count_odd_numbers(nums):
    count = 0
    for num in nums:
        if not num %2 == 0:
            count+=1
    return count

# test function
numbers = [2,10,11,56,98,23,22]
print(count_odd_numbers(numbers))