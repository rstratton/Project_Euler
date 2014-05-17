from time import time

def make_timed(f):
    def timed_f(*args):
        start_time = time()
        result = f(*args)
        stop_time = time()
        print('"' + str(f).split()[1] + '" time: {0} s'.format(stop_time-start_time))
        return result
    return timed_f

def memoize(f):
    cache = {}
    def memoized_f(*args):
        if not args in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized_f
