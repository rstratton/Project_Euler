isPrime :: Integral a => a -> Bool
isPrime n = length [i | i <- [2..(floor (sqrt n))], n `mod` i == 0] == 0
