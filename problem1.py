# String reverse without built in method

# Input: "python"
# Output: "nohtyp"

def reverse_string(s):
    print(s)
    result = ''
    for ch in s:
        result = ch + result
    return result

print(reverse_string("python"))
