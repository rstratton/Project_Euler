from toolkit.util import isPalindrome
from toolkit.digits import reverse

def isLychrel(n):
    for i in xrange(51):        
        n = n + reverse(n)
        if isPalindrome(n):
            return False
    return True
        
def countLychrels(n):
    count = 0
    for i in xrange(n):
        if isLychrel(i):
            count += 1
    return count

print(countLychrels(10000))
