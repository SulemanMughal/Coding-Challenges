def num_of_sublists(lst):
    return sum(1 for i in lst if type(i)==list)