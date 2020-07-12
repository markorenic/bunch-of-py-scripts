import random
board = []
playerOneTurn = True
endgame = False
turn = 0
for i in range (0, 9):
    board.append(str(i + 1))

def printBoard():
    print( '\n -----')
    print( '|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print( ' -----')
    print( '|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print( ' -----')
    print( '|' + board[6] + '|' + board[7] + '|' + board[8] + '|')
    print( ' -----\n')

def multiplayer():

    global playerOneTurn
    global endgame
    global turn
    player1 = str(input("Player one name: "))
    player2 = str(input("Player two name: "))

    while not endgame:
        printBoard()
        turn = turn + 1

        if playerOneTurn:
            print(player1 + " your turn: ")
        else :
            print(player2 + " your turn: ")

        try:
            choice = int(input(">> "))
        except:
            print("Please input a number 1-9: ")
            continue
        if board[choice - 1] == 'X' or board [choice-1] == 'O':
            print("That place is taken, please choose an empty one: ")
            continue

        if playerOneTurn:
            board[choice - 1] = 'X'
        else:
            board[choice - 1] = 'O'

        playerOneTurn = not playerOneTurn

        for i in range (0, 3) :
            j = i * 3
            if (board[j] == board[(j + 1)] and board[j] == board[(j + 2)]) :
                endgame = True
                printBoard()
            if (board[i] == board[(i + 3)] and board[i] == board[(i + 6)]) :
                endgame = True
                printBoard()

        if((board[0] == board[4] and board[0] == board[8]) or 
        (board[2] == board[4] and board[4] == board[6])) :
            endgame = True
            printBoard()


    print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")



def singleplayer():
    global playerOneTurn
    global endgame
    global turn
    fill = 0
    player1 = str(input("Player name:"))

    while not endgame:
        printBoard()
        turn = turn + 1

        if playerOneTurn:
            print(player1 + " your turn: ")
        else:
            print("CPU turn... ")

        try:
            if playerOneTurn:
                choice = int(input(">> "))
            else:                 
                for i in range (0,3):
                    #horizontal check
                    j = i * 3
                    if (board[j] == board[(j + 1)]):
                        if not(board[j+2] == "X" or board[j+2] == "O"):
                            choice = j+2
                            fill = 1
                    elif (board[j] == board[(j + 2)]):
                        if not(board[j+1] == "X" or board[j+1] == "O"):
                            choice = j+1
                            fill = 1
                    elif (board[j+1] == board[j+2]):
                        if not(board[j] == "X" or board[j] == "O"):
                            choice = j
                            fill = 1
                    print(choice)

                    #vertical
                    j = i * 3
                    if (board[i] == board[(i + 3)]):
                        if not(board[i+6] == "X" or board[i+6] == "O"):
                            choice = i+6
                            fill = 1
                    elif (board[i] == board[(i + 6)]):
                        if not(board[i+3] == "X" or board[i+3] == "O"):
                            choice = i+3
                            fill = 1
                    elif (board[i+3] == board[i+6]):
                        if not(board[i] == "X" or board[i] == "O"):
                            choice = i
                            fill = 1
                    print(choice)

                if not(fill == 1):
                    choice = random.randint(0,8)
                    print(choice)
                    while (board[choice] == "X" or board[choice] == "O"):
                        choice = random.randint(0,8)
                        print(choice)



        except:
            if playerOneTurn:
                print("Please input a number 1-9: ")
                continue
            else:
                pass

        if playerOneTurn:
            board[choice - 1] = 'X'
        else:
            board[choice] = 'O'

        playerOneTurn = not playerOneTurn

        for i in range (0, 3) :
            j = i * 3
            if (board[j] == board[(j + 1)] and board[j] == board[(j + 2)]) :
                endgame = True
                printBoard()
            if (board[i] == board[(i + 3)] and board[i] == board[(i + 6)]) :
                endgame = True
                printBoard()

        if((board[0] == board[4] and board[0] == board[8]) or 
        (board[2] == board[4] and board[4] == board[6])) :
            endgame = True
            printBoard()
    
    print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")



        

singleplayer()