def stock_picker(lst):
    return max([max(lst[i+1::])-lst[i] for i in range(len(lst)-1)]+[-1])