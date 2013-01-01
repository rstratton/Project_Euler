from performance import make_timed
from primes import primes_list, primes_dict
from math import sqrt, floor

PL = primes_list(1000000)
PD = primes_dict(1000000)

def is_pandigital(number):
    str_num = str(number)
    for i in range(1,len(str_num)+1):
        if not str(i) in str_num:
            return False
    return True

def is_prime(n):
    if n < 1000000:
        if n in PD:
            return True
        else:
            return False
    else:
        for i in PL:
            if n % i == 0:
                return False
        for i in range(1000001, int(sqrt(n)), 2):
            if n % i == 0:
                return False
        return True

def run():
    largest = 0
    for i in range(13, 9999999, 2):
        if is_pandigital(i) and is_prime(i):
            largest = i
        if (i - 1) % 1000000 == 0:
            print(i)
    return largest
        
