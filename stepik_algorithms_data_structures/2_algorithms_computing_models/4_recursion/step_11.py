def isPalindrome(s):
    if len(s) == 0:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindrome(s[1:-1])

s = input()

if isPalindrome(s):
    print(True)
else:
    print(False)