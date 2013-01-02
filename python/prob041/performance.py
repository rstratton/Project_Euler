from time import time

def make_timed(f):
    def timed_f(*args):
        start_time = time()
        result = f(*args)
        stop_time = time()
        print('"' + str(f).split()[1] + '" time: {0} s'.format(stop_time-start_time))
        return result
    return timed_f

def memoize(f):
    cache = {}
    def memoized_f(*args):
        if not args in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized_f

'''

class Polynomial(object):
    def __init__(self, coeff_list):
        self.coefficients = coeff_list

    def eval_at(self, x):
        result = 0
        for i in range(len(self.coefficients)):
            result += self.coefficients[i]*pow(x, i)
        return result

def sum_polynomials(a, b):
    coeff_list = []
    for i in range(min(len(a.coefficients), len(b.coefficients))):
        coeff_list.append(a.coefficients[i]+b.coefficients[i])
    if(len(a.coefficients) == len(b.coefficients)):
        return Polynomial(coeff_list)
    if(len(a.coefficients) > len(b.coefficients)):
        for i in range(len(b.coefficients), len(a.coefficients)):
            coeff_list.append(a.coefficients[i])
    else:
        for i in range(len(a.coefficients), len(b.coefficients)):
            coeff_list.append(b.coefficients[i])
    return Polynomial(coeff_list)

def mul_polynomial(p, c):
    coeff_list = []
    for i in range(len(p.coefficients)):
        coeff_list.append(p.coefficients[i] * c)
    return Polynomial(coeff_list)
    

def interpolate(points):

'''
    
