# AIM: A program that checks if a given string is a palindrome
def isPalindrome(s):
    return s == s[::-1] 
s = "car"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:   
    print("No")
