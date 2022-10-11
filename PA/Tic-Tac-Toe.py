import os

board_h = 3
board_w = 3
board = []
board_seq = []
alter = False

piece_to_be_deleted = (-1, -1)


def display():
    for i in range(board_h):
        for j in range(board_w):
            print(board[i][j], end=' ')
            if j != board_w - 1:
                print('|', end=' ')
        print('')
        if i != board_h - 1:
            for j in range(board_w * 2 - 1):
                if j % 2 == 1:
                    print("|", end=' ')
                else:
                    print("-", end=' ')
        print('')


def init_board():
    board.clear()
    for i in range(board_h):
        templist = []
        for j in range(board_w):
            templist.append('N')
        board.append(templist)
    board_seq.clear()
    for i in range(board_h):
        templist = []
        for j in range(board_w):
            templist.append(0)
        board_seq.append(templist)


def check_avalibility(x, y):
    return board[x][y] == 'N'


def set_piece(x, y, sign, step_size):
    if not check_avalibility(x, y):
        return False
    board[x][y] = sign
    board_seq[x][y] = step_size
    return True


def check_winner(sign):
    for i in range(board_h):
        flag_row = True
        for j in range(board_w):
            if board[i][j] != sign:
                flag_row = False
        if flag_row:
            return True
    for i in range(board_w):
        flag_col = True
        for j in range(board_h):
            if board[j][i] != sign:
                flag_col = False
        if flag_col:
            return True
    slant0 = True
    slant1 = True
    for i in range(board_h):
        if board[i][i] != sign:
            slant0 = False
        if board[i][board_w - i - 1] != sign:
            slant1 = False
    return slant0 or slant1


def clear_overtime(step):
    if step <= 6:
        return False
    for i in range(board_h):
        for j in range(board_w):
            if board_seq[i][j] <= step - 6 and board_seq[i][j] != 0:
                board[i][j] = 'N'
                board_seq[i][j] = 0


def about_to_be_deleted(step):
    x = -1
    y = -1
    for i in range(board_h):
        for j in range(board_w):
            if board_seq[i][j] <= step - 5 and board_seq[i][j] != 0:
                x = i
                y = j
    return (x, y)


def ask_player():
    player_input = input("")
    while (not player_input.isnumeric()) or int(player_input) > 8 or int(player_input) < 0:
        print("wrong input, you stupid! now input again")
        player_input = input("")

    in_x = int(player_input) // 3
    in_y = int(player_input) % 3
    return (in_x, in_y)


init_board()
print("Enable altered version?(限制棋子为6个)? Y/N")
alter_temp = input()
if alter_temp == 'Y' or alter_temp == 'y':
    alter = True

player = 'A'
step = 1
while True:
    os.system("clear")
    if not piece_to_be_deleted == (-1, -1):
        print("piece row=", piece_to_be_deleted[0], " col=", piece_to_be_deleted[1], " is going to be deleted")

    display()
    print("Player", player, " , Please input: [0-8]")
    player_choice = ask_player()
    player_x = player_choice[0]
    player_y = player_choice[1]
    if alter:
        print("alter mode! step=", step)
        clear_overtime(step)
        piece_to_be_deleted = about_to_be_deleted(step)
    while not set_piece(player_x, player_y, player, step):
        player_choice = ask_player()
        player_x = player_choice[0]
        player_y = player_choice[1]

    step += 1

    if check_winner(player):
        print(player, " winned!")
        print("\n\n clear bpard! \n\n")
        init_board()
        step = 1
    elif step == 10 and not alter:
        print("平局")
        print("\n\n clear bpard! \n\n")
        init_board()
        step = 1
    if player == 'A':
        player = 'B'
    else:
        player = 'A'
