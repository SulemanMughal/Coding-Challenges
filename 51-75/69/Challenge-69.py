def holey_sort(lst):
    d = {'0': 1, '4': 1, '6': 1, '8': 2, '9': 1}
    return sorted(lst, key=lambda x: sum(d.get(i, 0) for i in str(x)))