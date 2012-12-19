def str_div(a, b, p):
    """
        Returns a string representation of the quotient of a and b to 'p' places"""
    q = ''
    a = mod_x_ten(a,b)
    for i in range(p):
        q += str(a/b)
        a = mod_x_ten(a,b)
    return q

def mod_x_ten(a, b):
    return (a%b)*10

def dec_dig(a, b, d):
    """
        Returns the (d+1)'th digit to the right of the decimal point (0 = 1st, 1 = 2nd, etc.)"""
    if d == 0:
        return mod_x_ten(a,b)/b
    else:
        return dec_dig(mod_x_ten(a,b), b, d-1)

def next_dig(b, prev):
    return mod_x_ten(prev,b)/b

def pat_len(d):
    pat = ''
    index = 0
    while(True):
        pat += str(dec_dig(1,d,index))
        fract = str_div(1,d,4*index+1)
        rep1 = pat == fract[0:index+1]
        rep2 = pat == fract[index+1:2*index+1]
        rep3 = pat == fract[2*index+1:3*index+1]
        rep4 = pat == fract[3*index+1:4*index+1]
        if rep1 and rep2 and rep3 and rep4:
            return index+1
    
