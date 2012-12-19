def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

def sumnums(MAX):
    totalsum = 0
    for i in range(MAX):
        numstr = str(i)
        tempsum = 0
        for num in numstr:
            tempsum += factorial(int(num))
        if tempsum == i:
            print i
            totalsum += i
    print "Total is: ", totalsum
