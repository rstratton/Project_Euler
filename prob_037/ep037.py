from primes import primes_list, primes_dict

PRIMES_LIST = primes_list(1000000)
PRIMES_DICT = primes_dict(1000000)

def truncate_right(n):
    return int(str(n)[0:-1])

def truncate_left(n):
    return int(str(n)[1:])

def is_prime(n):
    return n in PRIMES_DICT

def is_truncatable(n):
    if '0' in str(n):
        return False
    if len(str(n)) < 2:
        return False
    return True

def is_truncatable_prime(n):
    if not is_truncatable(n):
        return False
    if not is_prime(n):
        return False
    left = truncate_left(n)
    right = truncate_right(n)
    while(is_truncatable(left)):
        if (not is_prime(left)) or (not is_prime(right)):
            return False
        left = truncate_left(left)
        right = truncate_right(right)
    if not is_prime(left) or not is_prime(right):
        return False
    else:
        return True

def truncatable_primes(n):
    t_primes = []
    for i in range(11, n+1):
        if is_truncatable_prime(i):
            t_primes.append(i)
    return t_primes
