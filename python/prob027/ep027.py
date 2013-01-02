from primes import make_erat
PRIMES = make_erat(500000)
print("Primes list made")

def eval_quad(b, c, n):
    return n**2 + b*n + c

def test_coeffs(b, c):
    consecutive = 0
    n = 0
    last_val = eval_quad(b, c, n)
    while last_val in PRIMES:
        consecutive += 1
        n += 1
        last_val = eval_quad(b, c, n)
    return consecutive

def coeff_comp():
    max_data = [0, 0, 0] #[max_primes, a, b]
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            consec_primes = test_coeffs(i, j)
            if consec_primes > max_data[0]:
                max_data[0] = consec_primes
                max_data[1] = i
                max_data[2] = j
    return max_data

def main():
    max_data = coeff_comp()
    print('b: {0}, c: {1}, max: {2}'.format(max_data[1], max_data[2], max_data[0]))
    
