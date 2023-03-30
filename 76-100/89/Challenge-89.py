from re import findall
    
def is_consecutive(s):
    for k in range(1, len(s)//2+1):
        n = list(map(int, findall(r'.{1,'+str(k)+'}', s)))
        if all(b-a == 1 for a, b in zip(n, n[1:])) or \
                all(b-a == -1 for a, b in zip(n, n[1:])): return True
    return False