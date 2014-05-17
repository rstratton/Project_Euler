import sys
sys.path.append('C:\\Users\\bob\\comp-sci\\project-euler\\toolkit')
from performance import memoize, make_timed

def next_num(n):
    return sum([x**2 for x in [int(n) for n in str(n)]])

next_num = memoize(next_num)

def solve(n):
    count = 0
    for i in range(1,n):
        while i not in (1, 89):
            i = next_num(i)
        if i == 89:
            count += 1
    return count

solve = make_timed(solve)
    
