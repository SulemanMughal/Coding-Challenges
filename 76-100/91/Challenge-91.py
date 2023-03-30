def digits(n):
    l = len(str(n))
    return n * l - int('1' * l)