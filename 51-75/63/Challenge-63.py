def min_miss_pos(lst):
    i = 1
    while True:
        if not i in lst:
            return i
        i += 1