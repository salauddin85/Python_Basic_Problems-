#  Problem 7: Count Vowels in a String
# Input: "Developer"
#  Output: 4

def count_vowels(s):
    if not s:
        return 0
    count = 0
    vowels = "aeiouAEIOU"  # Include both lowercase and uppercase vowels
    for char in s:
        if char in vowels:
            count += 1
    return count

# test function
print(count_vowels("Developer"))  # Output: 4