import time
from math import sqrt

def make_erat(n, timer=False):
    start_time = time.time()
    
    def elim_muls(n, m, li):
        for i in range(2*n, m, n):
            li[i] = 0

    nums = [0,0] + list(range(2, n+1))
    primes = []
    
    for i in range(2, len(nums)):
        if not nums[i] == 0:
            primes.append(i)
            elim_muls(i, n+1, nums)
            
    if timer:
        print(time.time() - start_time)
    dict_primes = {}
    for prime in primes:
        dict_primes[prime] = 0
    return dict_primes

