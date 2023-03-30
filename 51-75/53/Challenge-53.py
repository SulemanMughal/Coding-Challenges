def kempner(n, i=1, total=1):
    return max(1, i-1) if total%n == 0 else kempner(n, i+1, total*i)