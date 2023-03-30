def is_harshad(n):
    S = sum(map(int, str(n)))
    return not n % S