from primes import primes_list, primes_dict
from performance import memoize

P_LIST = primes_list(1000000)
P_DICT = {}
for i in range(len(P_LIST)):
    P_DICT[P_LIST[i]] = None

def prime_factors(n):
    pfs = {}
    
    if n in P_DICT:
        pfs[n] = None
        return pfs
    for i in range(len(P_LIST)):
        if n % P_LIST[i] == 0:
            pfs[P_LIST[i]] = None
            pfs.update(prime_factors(n//P_LIST[i]))
            break
    return pfs

#prime_factors = memoize(prime_factors)

def has_four_distinct(n):
    return len(prime_factors(n)) == 4

def solve():
    i = 647
    cur = False
    last1 = True
    last2 = True
    last3 = True
    while i < 1000000:
        #print(i)
        #print("   {0} {1} {2} {3}".format(last3, last2, last1, cur))
        i += 1
        last3 = last2
        last2 = last1
        last1 = cur
        cur = has_four_distinct(i)
        if cur and last1 and last2 and last3:
            print(i)
            break
