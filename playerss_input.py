def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1 enter marker X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')