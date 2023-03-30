def count_ones(lst):
    ones = ''.join(str(i) for i in lst).split('0')
    return sum(len(i) > 1 for i in ones)