from toolkit.digits import digitSum

def maxDigitSum(aRange, bRange):
    """Returns the maximal sum of digits over all numbers
    of the form pow(a, b), where a is in aRange and b is in
    bRange"""
    maxA, maxB, maxSum = 0, 0, 0
    for a in aRange:
        for b in bRange:
            thisSum = digitSum(pow(a, b))
            if thisSum > maxSum:
                maxA, maxB, maxSum = a, b, thisSum
    return maxA, maxB, maxSum
