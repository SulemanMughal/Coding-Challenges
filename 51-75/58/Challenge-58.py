def sum_primes(l):
    p = lambda x: 2 in [x, 2**x%x]
    return sum(filter(p, l)) if l else None