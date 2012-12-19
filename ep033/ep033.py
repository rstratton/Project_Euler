from fractions import gcd
import time

def is_curious(x):
	n = num(x)
	d = den(x)
	if int(str(n)[0]) == int(str(d)[1]) and not int(str(d)[0]) == 0:
		if n/d == int(str(n)[1])/int(str(d)[0]):
			return True
	if int(str(n)[1]) == int(str(d)[0]) and not int(str(d)[1]) == 0:
		if n/d == int(str(n)[0])/int(str(d)[1]):
			return True
	return False

def make_rat(x, y):
    return (x, y)

def num(x):
    return x[0]

def den(x):
    return x[1]

def mul_rat(x, y):
    product = make_rat(num(x)*num(y), den(x)*den(y))
    gcd_of_nums = gcd(num(product), den(product))
    return make_rat(num(product)/gcd_of_nums, den(product)/gcd_of_nums)

def test_curious():
    t = time.time()
    curious_fractions = []
    for i in range(10, 100):
        for j in range(i+1, 100):
            rat = make_rat(i, j)
            if is_curious(rat):
                curious_fractions.append(rat)
    print(time.time() - t)
    return curious_fractions
