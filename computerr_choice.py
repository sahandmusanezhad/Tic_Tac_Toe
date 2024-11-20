from spacee_check import space_check
from miniimax import minimax

def computer_choice(board, player_marker, computer_marker):
    best_score = -float('inf')
    best_move = None
    for i in range(1, 10):
        if space_check(board, i):
            board[i] = computer_marker
            score = minimax(board, 0, False, player_marker, computer_marker)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move
