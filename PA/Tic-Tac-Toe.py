board_h=3
board_w=3
board = []
board_seq = []
alter = False
def display():
    for i in range(board_h):
        for j in range(board_w):
            print(board[i][j], end = ' ')
            if j != board_w -1:
                print('|', end = ' ')
        print('')
        if i != board_h-1:
            for j in range(board_w*2-1):
                if j % 2 ==1:
                    print("|",end=' ')
                else:
                    print("-",end=' ')
        print('')

def init_board():
    board.clear()
    for i in range(board_h):
        templist=[]
        for j in range(board_w):
            templist.append('N')
        board.append(templist)
    board_seq.clear()
    for i in range(board_h):
        templist=[]
        for j in range(board_w):
            templist.append(0)
        board_seq.append(templist)

def check_avalibility(x,y):
    return board[x][y] == 'N'
def set_piece(x,y,sign,step):
    if not check_avalibility(x,y):
        return False
    board[x][y] = sign
    board_seq[x][y] = step
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
            slant0=False
        if board[i][board_w-i-1] != sign:
            slant1=False
    return slant0 or slant1

def clear_overtime(step):
    if step <= 6:
        return False
    for i in range(board_h):
        for j in range(board_w):
            if board_seq[i][j] <= step-6 and board_seq[i][j] != 0:
                board[i][j] = 'N'
                board_seq[i][j] = 0
                print("i",i,"j",j,"cleared!")


init_board()
print("Enable altered version?(限制棋子为6个)? Y/N")
alter_temp = input()
if alter_temp == 'Y' or alter_temp == 'y':
    alter = True

player = 'A'
step = 1
while True:
    display()
    print("Player",player," , Please input:")
    player_x = int(input("x=?[0,2],int"))
    player_y = int(input("y=?[0,2],int"))
    while (not set_piece(player_x,player_y,player,step)):
        print("Player", player, " , Please input:")
        player_x = int(input("x=?[0,2],int"))
        player_y = int(input("y=?[0,2],int"))
    if alter:
        print("alter mode! step=",step)
        clear_overtime(step)
    step += 1

    if check_winner(player):
        print(player," winned!")
        print("\n\n clear bpard! \n\n")
        init_board()
        step = 1
    if player == 'A':
        player = 'B'
    else:
        player = 'A'
