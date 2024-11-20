from spacee_check import space_check
from winn_check import win_check
from full_board_checkk import full_board_check

def minimax(board, depth, is_maximizing, player_marker, computer_marker):
    if win_check(board, computer_marker):
        return 10 - depth
    elif win_check(board, player_marker):
        return depth - 10
    elif full_board_check(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(1, 10):
            if space_check(board, i):
                board[i] = computer_marker
                score = minimax(board, depth + 1, False, player_marker, computer_marker)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(1, 10):
            if space_check(board, i):
                board[i] = player_marker
                score = minimax(board, depth + 1, True, player_marker, computer_marker)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score
