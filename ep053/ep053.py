from math import factorial as fact

def C(n,r):
    return fact(n)/(fact(n-r)*fact(r))

count = 0
for n in range(1, 101):
    for r in range(1, n):
        if C(n,r) > 1000000:
            count += 1

print(count)
