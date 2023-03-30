def find_fulcrum(lst):
    for idx, i in enumerate(lst):
        if sum(lst[:idx]) == sum(lst[idx+1:]):
            return i
    return -1