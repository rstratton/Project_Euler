from performance import make_timed

def is_pandigital(n):
    string = str(n)
    return len(string) == 9 and \
           '1' in string and \
           '2' in string and \
           '3' in string and \
           '4' in string and \
           '5' in string and \
           '6' in string and \
           '7' in string and \
           '8' in string and \
           '9' in string

def concat_product(x, n):
    result = ''
    for i in range(1,n+1):
        result += str(x*i)
    return int(result)

def run():
    largest = 0
    for i in range(2,12):
        last_result = 0
        x = 1
        while len(str(last_result)) <= 9:
            last_result = concat_product(x, i)
            if is_pandigital(last_result) and last_result > largest:
                largest = last_result
            x += 1
    return largest

                
