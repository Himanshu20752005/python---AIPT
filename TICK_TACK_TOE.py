
board = ["_","_","_","_","_","_","_","_","_"]
current = 'x'
won = 1

def board_display():
    print(board[0]+"  |   "+board[1]+"    |  "+board[2])
    print("___________________")
    print(board[3] + "  |   " + board[4] + "    |  " + board[5])
    print("___________________")
    print(board[6] + "  |   " + board[7] + "    |  " + board[8])

def initialize_move():
    inpt = int(input("Enter the Position (1-9) : "))
    if board[inpt-1] == "_" :
        board[inpt-1] = current
    else:
        print("Slot is full , make another move !!")
        initialize_move()

def winning_conditions():
    global won
    #horizontal conditions for winning
    if board[0]==board[1]==board[2]=='x' or board[0]==board[1]==board[2]=='o' :
        print(current +" won")
        won = 0
    elif board[3]==board[4]==board[5]=='x' or board[3]==board[4]==board[5]=='o':
        print(current + " won")
        won = 0
    elif board[6] == board[7] == board[8] == 'x' or board[6] == board[7] == board[8] == 'o':
        print(current + " won")
        won = 0

    #vertical conditions for winning
    if board[0]==board[3]==board[6]=='x' or board[0]==board[3]==board[6]=='o' :
        print(current + " won")
        won = 0
    elif board[1]==board[4]==board[7]=='x' or board[1]==board[4]==board[7]=='o' :
        print(current + " won")
        won = 0
    elif board[2]==board[5]==board[8]=='x' or board[2]==board[5]==board[8]=='o' :
        print(current + " won")
        won = 0

    #diagonal conditions for winning
    if board[0]==board[4]==board[8]=='x' or board[0]==board[4]==board[8]=='o' :
        print(current + " won")
        won = 0
    elif board[2]==board[4]==board[6]=='x' or board[2]==board[4]==board[6]=='o' :
        print(current + " won")
        won = 0

while won!=0 :
    board_display()
    if current == 'x':
        print("Turn - X")
        initialize_move()
        winning_conditions()
        current ='o'
    elif current == 'o':
        print("Turn - O")
        initialize_move()
        winning_conditions()
        current ='x'
