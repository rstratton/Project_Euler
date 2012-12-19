TABLE_SIZE = 3000

def p(n):
    return (n*(3*n-1))//2

P_LIST = [p(n) for n in range(1,TABLE_SIZE)]
P_DICT = {}
for i in range(len(P_LIST)):
    P_DICT[P_LIST[i]] = 0

best_guess = (0, 0)
difference = 100000000

for dist in range(1, TABLE_SIZE - 2):
    for i in range(0,TABLE_SIZE - dist -1):
        (p1, p2) = (P_LIST[i], P_LIST[i + dist])
        if p2 + p1 in P_DICT and p2 - p1 in P_DICT and p2 - p1 < difference:
            best_guess = (p1, p2)
            difference = p2 - p1

print(difference)
    
