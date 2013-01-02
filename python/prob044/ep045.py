def T(n):
    return (n*(n+1))//2

def P(n):
    return (n*(3*n-1))//2

def H(n):
    return n*(2*n-1)

TABLE_SIZE = 100000

T_LIST = [T(n) for n in range(1, TABLE_SIZE)]
P_LIST = [P(n) for n in range(1, TABLE_SIZE)]
H_LIST = [H(n) for n in range(1, TABLE_SIZE)]

T_DICT = {}
P_DICT = {}
H_DICT = {}

for i in range(0, TABLE_SIZE - 1):
    T_DICT[T_LIST[i]] = None
    P_DICT[P_LIST[i]] = None
    H_DICT[H_LIST[i]] = None

largest = 40755
for entry in H_LIST:
    if entry in P_DICT and entry in T_DICT and entry > largest:
        largest = entry
        break;

print(largest)
