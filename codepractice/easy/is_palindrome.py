
def isPalindrome(string):
    return string[::-1] == string

test0 = 'aabbaa'
test1 = 'abcb'
print(isPalindrome(test0))
print(isPalindrome(test1))