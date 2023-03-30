def split_bunches(bunches):
    res = []
    for fruit in bunches:
        res += [{'name': fruit['name'], 'quantity': 1}] * fruit['quantity']
    return res