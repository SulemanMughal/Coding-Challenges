def num_split(num):
    f,res = [1,-1][num < 0],[]
    num = abs(num)
    while num:
        num,r = divmod(num,10)
        res = [r*f]+res
        f *= 10
    return res