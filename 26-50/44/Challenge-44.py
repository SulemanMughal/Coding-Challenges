def circular_shift(lst1, lst2, n):
    return lst1 == lst2[n:] + lst2[:n]