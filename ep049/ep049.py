from primes import Primes
from performance import memoize
from itertools import permutations as list_perms
p = Primes(10000)
is_prime = p.is_prime
p_list = p.primes_list

def permutations(n):
    return {int(''.join(x)): None for x in list(list_perms(str(n))) if x[0] != '0'}

permutations = memoize(permutations)

def solve():
    results = []
    for delta in range(3330, 5000):
        for i in range(1000, 10000 - 2*delta):
            perms = permutations(i)
            if (is_prime(i) and is_prime(i + delta) and is_prime(i + 2*delta) and
                (i+delta) in perms and (i+2*delta) in perms):
                results.append((i, i+delta, i+2*delta))
                print(i, i+delta, i+2*delta)
    return results
                
