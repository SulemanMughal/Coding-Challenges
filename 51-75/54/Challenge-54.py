def pairs(lst):
    return [[lst[i], lst[-(i+1)]] for i in range((len(lst)+1) //  2)]