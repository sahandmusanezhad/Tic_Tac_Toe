def win_check(board, mark):

    return (
    # check across the top
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    # check across the middle
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    # check across the bottom
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    # check down the middle
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    # check down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    # check down the right side
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    # diagonal
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)
    )