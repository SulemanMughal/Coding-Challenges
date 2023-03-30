def digit_sort(lst):
    return sorted(lst, key=lambda x: (-len(str(x)), x))