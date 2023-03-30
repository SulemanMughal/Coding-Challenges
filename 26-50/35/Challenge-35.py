def digit_occurrences(start, end, digit):
    return ''.join(str(i) for i in range(start,end+1)).count(str(digit))