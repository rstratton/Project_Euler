from primes import primes_list, primes_dict

P_LIST = primes_list(100000)
P_DICT = primes_dict(100000)

S_LIST = [2*(n**2) for n in range(1,100000)]
S_DICT = {}
for i in range(len(S_LIST)):
    S_DICT[S_LIST[i]] = None

def test(n):
    for prime in P_LIST:
        if prime > n:
            break
        for sq in S_LIST:
            if prime + sq > n:
                break
            if prime + sq == n:
                return True
    return False

for i in range(33, 1000000, 2):
    if i in P_DICT:
        continue
    if not test(i):
        print(i)
        break
    

