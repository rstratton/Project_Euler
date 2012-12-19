from toolkit.primes import Primes
from toolkit import util

MAX_DIGITS = 6
MAX_VAL = 10**MAX_DIGITS - 1
p = Primes(MAX_VAL)

previous_nums = set()

for num in range(MAX_VAL):
    if num in previous_nums:
        continue
    else:
        previous_nums.add(num)
    
    for bitString 
