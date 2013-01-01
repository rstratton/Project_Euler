#!/usr/bin/python3

"""
===========================
Project Euler - Problem 001
---------------------------
Description: Find the sum of all the multiples of 3 or 5 below 1000.
===========================
"""

def solution1():
    """
    Return the sum of all the multiples of 3 or 5 below 'lim'
    """
    return sum([n for n in range(1,1000) if n % 3 == 0 or n % 5 == 0])

def solution2():
    """
    Return the sum of all the multiples of 3 or 5 below 'lim'
    """
    total = 0
    for n in range(1,1000):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    return total

print(solution1())
print(solution2())
