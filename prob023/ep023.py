from performance import make_timed, memoize
from primes import primes_list, primes_dict
MAX_NUM = 28123
P_LIST = primes_list(MAX_NUM)
P_DICT = primes_dict(MAX_NUM)

def sum_prop_divs(n):
    return sum(proper_divisors(n))

def proper_divisors(n):
    p_factors = prime_factors(n)
    divisors = {}
    width = len(p_factors)
    for i in range(2**width-1):
        divisor = choose_factors(p_factors, binary_str(i, width))
        divisors[divisor] = None
    return list(divisors.keys())
        
def choose_factors(factors, bit_str):
    product = 1
    for i in range(len(factors)):
        if bit_str[i] == '1':
            product *= factors[i]
    return product

def binary_str(value, length):
    return str(bin(value))[2:].zfill(length)

def prime_factors(n, primes_list=P_LIST, primes_dict=P_DICT):
    factors = []
    if n == 1 or n == 0:
        return []
    if n in primes_dict:
        return [n]
    for p in primes_list:
        if n % p == 0:
            factors.append(p)
            break
    factors.extend(prime_factors(n//p))
    return factors

def is_abundant(n):
    return sum_prop_divs(n) > n

def is_perfect(n):
    return sum_prop_divs(n) == n

def make_abund_structures(n):
    abund_dict = {}
    for i in range(12, n+1):
        if (i not in abund_dict) and is_abundant(i):
            j = 1
            while(j*i < n):
                abund_dict[j*i] = None
                j += 1
        if is_perfect(i):
            j = 2
            while(j*i < n):
                abund_dict[j*i] = None
                j += 1
    abund_list = list(abund_dict.keys())
    abund_list.sort()
    return (abund_list, abund_dict)

binary_str = memoize(binary_str)
prime_factors = memoize(prime_factors)
sum_prop_divs = memoize(sum_prop_divs)
make_abund_structures = make_timed(make_abund_structures)

ABUND_LIST, ABUND_DICT = make_abund_structures(MAX_NUM)

def is_sum_of_abund(n, abund_list=ABUND_LIST):
    for a in abund_list:
        if a > n:
            return False
        for b in abund_list:
            if a + b > n:
                break
            if a + b == n:
                return True
    return False

def nums_not_sum_of_abund(n, abund_list=ABUND_LIST):
    num_list = list(range(n+1))
    for a in abund_list:
        if a > n:
            break
        for b in abund_list:
            if a + b > n:
                break
            num_list[a+b] = -1
    final_list = []
    for i in range(len(num_list)):
        if not num_list[i] == -1:
            final_list.append(i)
    return final_list

print(sum(nums_not_sum_of_abund(MAX_NUM)))
