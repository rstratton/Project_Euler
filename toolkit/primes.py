from math import sqrt

class Primes:
    def __init__(self, n):
        (self.primes_list, self.primes_dict) = make_primes(n)

    def is_prime(self, n):
        return n in self.primes_dict

    def primes_list(self):
        return self.primes_list
        
def make_primes(n):
    def elim_muls(n, m, li):
        for i in range(2*n, m, n):
            li[i] = 0

    nums = [0,0] + list(range(2, n+1))
    primes = []
    
    for i in range(2, len(nums)):
        if not nums[i] == 0:
            primes.append(i)
            elim_muls(i, n+1, nums)
    p_dict = {}
    for prime in primes:
        p_dict[prime] = None
    return (primes, p_dict)

