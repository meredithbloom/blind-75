# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
    new_string = ''.join(letter for letter in s if letter.isalnum())
    new_string = new_string.lower()
    flipped = new_string[::-1]
    if new_string == flipped:
        return True
    else:
        return False




input1 = "A man, a plan, a canal: Panama"
input2 = "race a car"
input3 = " "

isPalindrome(input1)
isPalindrome(input2)
isPalindrome(input3)