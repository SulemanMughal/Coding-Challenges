def bridges(s):
    arr = s.split('/')
    hori = sum(set(i) == {'#'} for i in arr)
    vert = sum(set(i) == {'#'} for i in zip(*arr))
    return hori + vert