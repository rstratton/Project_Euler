def isPalindrome(n):
    word = str(n)
    for i in xrange(len(word)//2 + 1):
        if not word[i] == word[len(word)-1-i]:
            return False
    return True

def bitStringList(n):
    '''
    Create a list of all bit strings of
    length n.
    '''
    if n < 0:
        return list()
    li = list()
    for val in range(2**n - 1):
        # Append the zero-padded binary representation of "val" to our list
        li.append(bin(val)[2:].zfill(n))
    return li
    
