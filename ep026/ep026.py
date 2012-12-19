def pat_len(d):
    a = 1
    a_hist = []
    while(True):
        a = (a%d)*10
        if a == 0:
            return 0
        if a in a_hist:
            return len(a_hist[a_hist.index(a):len(a_hist)])
        a_hist.append(a)
