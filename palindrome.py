def is_palindrome(string):
    # The following lines checks to see if after reversing the string, it is still the same
    if string == string[::-1]:
        return True
    else:
        return False
    # An example usage
print(is_palindrome("racecar"))