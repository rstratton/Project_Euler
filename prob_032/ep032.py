def len_nums(a, b, c):
    return len(str(a) + str(b) + str(c))
def is_pan(a, b, c):
    string = str(a) + str(b) + str(c)
    for i in range(1, 10):
        if not string.count(str(i)) == 1:
            return False
    return True

prods = []
for i in range(2, 5000):
    for j in range(i+1, 5000):
        if len_nums(i,j,i*j) == 9 and is_pan(i, j, i*j):
            if not i*j in prods:
                prods.append(i*j)

print(sum(prods))
