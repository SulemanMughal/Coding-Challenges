def palindrome_type(n):
    b, d = [s == s[::-1] for s in [str(n), bin(n)[2:]]]
    return ['Neither!','Binary only.','Decimal only.','Decimal and binary.'][d + 2 * b]