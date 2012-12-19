def b2tob10(b2num):
    b2str = str(b2num)
    b10num = 0
    for i in range(len(b2str)):
        b10num += int(b2str[i]) * pow(2, len(b2str)-(i+1))
    return b10num

def ispalin(num):
    numstr = str(num)
    for i in range(len(numstr)):
        if not numstr[i] == numstr[len(numstr)-1-i]:
            return False
    return True

def b10tob2(b10num):
    b2list = []
    while not b10num == 0:
        b2list.insert(0,b10num%2)
        b10num /= 2
    for elem in b2list:
        b2list[b2list.index(elem)] = str(b2list[b2list.index(elem)])
    return int("".join(b2list))

def main():
    sm = 0
    for i in range(1,999999):
        if ispalin(i) and ispalin(b10tob2(i)):
            sm += i
    print sm

    
