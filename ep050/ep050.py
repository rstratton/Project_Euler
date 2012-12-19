import sys
sys.path.append('C:\\Users\\bob\\comp-sci\\project-euler\\toolkit')
from primes import Primes

p = Primes(1000000)
is_prime = p.is_prime
p_list = p.primes_list

def solve():
    most_terms, prime = 0, 0
    for terms in range(1, 547):
        for i in range(len(p_list) - terms):
            p_sum = sum(p_list[i:i+terms])
            if p_sum > 1000000:
                break
            if is_prime(p_sum):
                most_terms, prime = terms, p_sum
                break
    return prime

