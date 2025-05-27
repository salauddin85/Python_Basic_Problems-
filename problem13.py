# find 2nd maximum number in the list without sort

def second_maximum(nums):
    if len(nums) < 2:
        return None  # Second max not possible 

    max1 = float('-inf')
    max2 = float('-inf')

    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    return max2 if max2 != float('-inf') else None

# Test
nums = [2, 6, 3, 1, 22, 34]
print("Second Maximum:", second_maximum(nums))
