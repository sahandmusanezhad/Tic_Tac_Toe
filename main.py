from display import display_board
from firstchoose import choose_first
from full_board_checkk import full_board_check
from placee_marker import place_marker
from player_choicee import player_choice
from playerss_input import player_input
from raplayy import replay
from winn_check import win_check
from computerr_choice import computer_choice

print('Welcome to Tic Tac Toe')

# play the game
while True:

    ## set everything is up (board, who is first, choose markers X,O)
    the_board = [' ']*10
    player1_marker,computer_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n? ')
    if play_game == 'y':
      game_on = True
    else:
      game_on = False

    ## game play

    while game_on:

        ### player one turn
        if turn == 'Player 1':

            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player1_marker, position)
            # check if the won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 wins!')
                game_on = False
            # or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    break
                # no tie and no win? then next player`s turn
                else:
                    turn = 'Computer'

        else:
          # Computer's turn
            position = computer_choice(the_board, player1_marker, computer_marker)
            place_marker(the_board, computer_marker, position)
            if win_check(the_board, computer_marker):
                display_board(the_board)
                print('The computer has beaten you! You lose.')
                game_on = False
            else:
                 if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                 else:
                    turn = 'Player 1'

    if not replay():
        break