def freq_count(lst, el):
    
    level = 0
    res = []
    while lst:
        res.append([level, lst.count(el)])
        level += 1
        lst = [
            x for l in lst if isinstance(l, list)
            for x in l
        ]
    return res