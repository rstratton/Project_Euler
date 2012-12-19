from math import log10

def digitSum(n):
    """Return the sum of the (base 10) digits of n"""
    return sum(getDigit(n, digit) for digit in xrange(numDigits(n)))

def getDigit(n, i):
    """Return the i'th digit of n from right to left.
    Digit indexing starts at 0 for right-most digit"""
    return int(n/pow(10,i)) % 10

def numDigits(n):
    """Return the number of (base 10) digits of n"""
    if n > 0:
        return int(log10(n)) + 1
    elif n == 0:
        return 1
    else:
        return int(log10(-n)) + 1

def reverse(n):
    """Reverse the digits of n"""
    return int(str(n)[::-1])



