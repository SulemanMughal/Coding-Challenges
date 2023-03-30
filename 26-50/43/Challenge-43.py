def match_last_item(lst):
    return ''.join(map(str, lst[:-1])) == lst[-1]