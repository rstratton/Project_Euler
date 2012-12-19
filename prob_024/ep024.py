def inttolist(i):
    return list(str(10))

def listtoint(li):
    return (int("".join(li)))

def inttostr(i):
    return str(i)

def strtoint(st):
    return int(st)

def b10tob2(b10num):
    b2num = ""
    while not (b10num == 0):
        b2num = str(b10num % 2) + b2num
        b10num = str(b10num / 2)
    return int(b2num)

def b2tob10(b2num):
    b10list = []
    b2list = []
    while not (b2num == 0):
        b2list = inttolist(b2num)
        b2list.reverse()
        
    
        

