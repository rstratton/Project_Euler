"""
==========================
Project Euler - Problem 1:
==========================
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def solution1(lim):
    """
    Return the sum of all the multiples of 3 or 5 below 'lim'
    """
    return sum([n for n in xrange(1,lim) if n % 3 == 0 or n % 5 == 0])

def solution2(lim):
    """
    Return the sum of all the multiples of 3 or 5 below 'lim'
    """
    total = 0
    for n in xrange(1,lim):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    return total

x = input("Gimme")
print(x)
