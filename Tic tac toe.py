#tic tac toe

def displayBoard(board):
    for i in range(3):
        print("|",board[i][0], "|" ,board[i][1],"|", board[i][2],"|")
        print("-------------")


def checkWin(board):
    for i in range(3):
        #rows
        if board[i][0] == board[i][1] == board[i][2] != " " :
            return True            
    for j in range(3):
        #columns
        if board[0][j] == board[1][j] == board[2][j] != " " :
            return True            
    #diagonals
    if board[0][0] == board[1][1] == board[2][2] != " " :
        return True      
            
    if board[0][2] == board[1][1] == board[2][0] != " " :
        return True
    return False

def tictactoe():
    board=[[" "," "," "],
           [" "," "," "],
           [" "," "," "]]
    player="X"

    while not checkWin(board):
        displayBoard(board)
        print("Player", player,"'s chance")
        enter_row=int(input("Enter the row number (0,1,2):"))
        enter_col=int(input("Enter the column number(0,1,2):"))
        if board[enter_row][enter_col]==" ":
            board[enter_row][enter_col]= player
            if player=="X":
                player="O"
            else:
                player="X"
        else:
            print("That spot is already taken. Try again.")
    displayBoard(board)
    print("-------------")
    print("Congratulations",player,"wins the game")

tictactoe()
