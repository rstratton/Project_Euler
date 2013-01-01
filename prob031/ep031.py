coins = [1, 2, 5, 10, 20, 50, 100, 200]
def num_combos(goal, total=0, max_coin=200):
    '''Returns the number of ways the quantity n
    may be reached using any combination of coins
    '''
    combinations = 0
    if total == goal:
        return 1
    for coin in [c for c in coins if c <= goal-total and c <= max_coin]:
        combinations += num_combos(goal, total + coin, coin)
    return combinations
