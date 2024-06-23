# Palindrome of a string

def is_palindrome(s):

    # Remove spaces and convert to lower for comparison
    s = s.replace(" ", "").lower()
    # check if the reverse is same as original
    # print(s[::-1])
    return s == s[::-1]


print(is_palindrome('Naman')) # True
print(is_palindrome('Namo')) # False

