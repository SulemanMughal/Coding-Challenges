def consecutive_combo(lst1, lst2):
    lst3 = lst1 + lst2
    return max(lst3) - min(lst3) == len(lst3) - 1