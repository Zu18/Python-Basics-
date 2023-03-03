# Write a function that checks if a given string (case insensitive) is a palindrome.


def is_palindrome(s):
    if s.lower() == s[::-1].lower():
        return True
    else:
        return False



print(is_palindrome("ag"))