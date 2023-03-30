def checker_board(n, el1, el2):
    if el1==el2: return 'invalid'
    return [[el2 if (i+j)%2 else el1 for i in range(n)] for j in range(n)]