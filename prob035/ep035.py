from primes import primes_list, primes_dict
PRIMES_LIST = primes_list(999999)
PRIMES_DICT = primes_dict(999999)
print("Primes list and dict built")

def shift_one(num):
    str_num = str(num)
    cycled_num_str = str_num[1:len(str_num)] + str_num[0]
    return int(cycled_num_str)

def is_cyclic_prime(prime):
    shifted = prime
    if '0' in str(prime):
        return False
    for _ in range(len(str(prime))+2):
        shifted = shift_one(shifted)
        if shifted not in PRIMES_DICT:
            return False
    return True

def check_all_primes(n, print_circular=False):
    cyclic_count = 0
    for prime in PRIMES_LIST:
        if prime > n:
            break
        if is_cyclic_prime(prime):
            if print_circular:
                print(prime)
            cyclic_count += 1
    return cyclic_count

def run():
    return check_all_primes(1000000)
