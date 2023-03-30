def split(txt):
    a = []
    b = ""
    for i in txt:
        b += i
        if b.count("(") == b.count(")"):
            a.append(b)
            b = ""
    return a