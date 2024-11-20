from spacee_check import space_check

def player_choice(board):

    postion = 0

    while postion not in [1,2,3,4,5,6,7,8,9] or not space_check(board,postion):
        postion = int(input('Choose a position: (1,9) '))

    return postion