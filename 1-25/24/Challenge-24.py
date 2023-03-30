def next_in_line(lst, num):
    return lst[1:] + [num] if lst else "No list has been selected"