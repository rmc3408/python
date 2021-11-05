import random as r


end = True
marker = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player_name = ['', '']


def display_board():

    print(f'        {marker[0]}       |        {marker[1]}       |        {marker[2]}       ')
    print(f'----------------|----------------|----------------')
    print(f'        {marker[3]}       |        {marker[4]}       |        {marker[5]}       ')
    print(f'----------------|----------------|----------------')
    print(f'        {marker[6]}       |        {marker[7]}       |        {marker[8]}       ')


def choice_start():
    first = r.randrange(1, 3)

    player_a = input("Player name ?")
    player_b = input("Player name ?")
    
    if first == 1:
        player_name[0] = player_a
        player_name[1] = player_b
    else:
        player_name[1] = player_a
        player_name[0] = player_b


choice_start()


def turn_player_one():
    player_choice = int(input(f'Enter board location, {player_name[0]} ?'))
    marker[player_choice-1] = 1
    return check_winner(1)


def turn_player_two():
    player_choice = int(input(f'Enter board location, {player_name[1]} ?'))
    marker[player_choice-1] = 2
    return check_winner(2)


def check_winner(num):
    g = num
    if (marker[0] == g and marker[1] == g and marker[2] == g) or \
    (marker[3]==g and marker[4]==g and marker[5]==g) or \
    (marker[6]==g and marker[7]==g and marker[8]==g) or \
    (marker[0]==g and marker[3]==g and marker[6]==g) or \
    (marker[1]==g and marker[4]==g and marker[7]==g) or \
    (marker[2]==g and marker[5]==g and marker[8]==g) or \
    (marker[0]==g and marker[4]==g and marker[8]==g) or \
    (marker[2]==g and marker[4]==g and marker[6]==g) in marker:
        message_winner()
        return False
    else:
        return True


def message_winner():
    print(f'------------> WIN <----------------\n'*20)
    

while end:
    print('\n'*10)
    display_board()
    print('\n'*1)
    end = turn_player_one()

    if not end:
        break
    else:
        print('\n'*10)
        display_board()
        print('\n'*1)
        end = turn_player_two()

