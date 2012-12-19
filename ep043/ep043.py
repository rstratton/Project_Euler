def has_property(n):
    str_n = str(n)
    sub1 = int(str_n[1:4])
    sub2 = int(str_n[2:5])
    sub3 = int(str_n[3:6])
    sub4 = int(str_n[4:7])
    sub5 = int(str_n[5:8])
    sub6 = int(str_n[6:9])
    sub7 = int(str_n[7:10])
    if sub1 % 2 != 0:
        return False
    if sub2 % 3 != 0:
        return False
    if sub3 % 5 != 0:
        return False
    if sub4 % 7 != 0:
        return False
    if sub5 % 11 != 0:
        return False
    if sub6 % 13 != 0:
        return False
    if sub7 % 17 != 0:
        return False
    return True

def is_pandigital(n):
    if n % 9 != 0:
        return False
    digit_sum = 0
    n_copy = n
    while n_copy > 0:
        digit_sum += n_copy % 10
        n_copy //= 10
    if digit_sum != 45:
        return False
    str_n = str(n)
    for i in range(10):
        if str(i) not in str_n:
            return False
    return True

def generate_permutations(digits=['0','1','2','3','4',
                                  '5','6','7','8','9']):
    if len(digits) == 1:
        return digits
    permutations = []
    for digit in digits:
        digits_copy = digits[:]
        digits_copy.remove(digit)
        perms = generate_permutations(digits_copy)
        for perm in perms:
            new_perm = perm + digit
            permutations.append(new_perm)
    return permutations

def strings_to_numbers(strings):
    result = []
    for string in strings:
        if string[0] == '0':
            continue
        result.append(int(string))
    return result    

def run():
    pandigitals = strings_to_numbers(generate_permutations())
    total_sum = 0
    for num in pandigitals:
        if has_property(num):
            total_sum += num
    return total_sum
