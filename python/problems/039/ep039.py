from math import floor, ceil, sqrt

def number_of_solutions(p):
    solution_count = 0
    for a in range(1, int(floor( ((2-sqrt(2))/2)*p ))):
        b = (p*p - 2*a*p)/(2*p - 2*a)
        c = p - a - b
        if floor(b) == b and floor(c) == c:
            solution_count += 1
    return solution_count
        

def is_pythag_triple(a, b, c):
    return a*a + b*b == c*c

def run():
    max_solutions = 0
    max_perimter = 0
    for p in range(10,1001):
        num_solutions = number_of_solutions(p)
        if num_solutions > max_solutions:
            max_solutions = num_solutions
            max_perimeter = p
    return max_perimeter
