def tic_tac_toe(board):
    rows = [set(i) for i in board]
    cols = [set(i) for i in zip(*board)]
    diag = [set(board[i][i] for i in range(3)),
            set(board[i][i] for i in range(-1, -4, -1))]
            
    for i in rows + cols + diag:
        if len(i) == 1 and 'E' not in i:
            return i.pop()
            
    return 'Draw'