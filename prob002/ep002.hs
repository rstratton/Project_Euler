fib n = fibs !! n
fibs = 1 : 1 : zipWith (+) fibs (tail fibs)

