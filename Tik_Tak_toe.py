theBoard = { '7' : ' ' , '8' : ' ' , '9' : ' ' ,
             '4' : ' ' , '5' : ' ' , '6' : ' ' ,
             '1' : ' ' , '2' : ' ' , '3' : ' ' }

board_key = []

for key in theBoard:
    board_key.append(key)

def printBoard(board): 
    print( board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print( board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print( board['1'] + '|' + board['2'] + '|' + board['3'])


def game():

    turn = 'X'

    count = 0

    for i in range(10):

        printBoard(theBoard)

        print('Now ! its your turn' + turn + '. move to which place?')

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count+=1

        else:
            print('the place is already filled, choose another place')
            continue

        if count >= 5:
            if ( theBoard['7'] == theBoard['8'] == theBoard['9'] == ' '):  #across top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print('*****'  +  turn + 'won. *****')
                break

            elif ( theBoard['4'] == theBoard['5'] == theBoard['6'] == ' '):  #across middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print('*****'  +  turn + 'won. *****')
                break
            elif ( theBoard['1'] == theBoard['2'] == theBoard['3'] == ' '):  #across bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print('*****'  +  turn + 'won. *****')
                break
            elif ( theBoard['7'] == theBoard['4'] == theBoard['1'] == ' '):  #across left down
                printBoard(theBoard)
                print("\nGame Over.\n")
                print('*****'  +  turn + 'won. *****')
                break
            elif ( theBoard['8'] == theBoard['5'] == theBoard['2'] == ' '):  #across middle top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print('*****'  +  turn + 'won. *****')
                break
            elif ( theBoard['9'] == theBoard['6'] == theBoard['3'] == ' '):  #across right bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print('*****'  +  turn + 'won. *****')
                break
            elif ( theBoard['9'] == theBoard['5'] == theBoard['1'] == ' '):  #diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print('*****'  +  turn + 'won. *****')
                break

            elif ( theBoard['7'] == theBoard['5'] == theBoard['3'] == ' '):  #diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print('*****'  +  turn + 'won. *****')
                break

            else:
                printBoard(theBoard)
               
                print('*****'  +  turn + 'won. *****')
                break

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")



        if turn == 'X':
            turn = 'O'

        else:
            turn = 'X'





    restart = input('do want to play again')

    if restart == 'Y' or restart == 'y':
        for key in board_key:
            theBoard[key] = ' '

            # for key in theBoard:
            #     board_key.append(key) 
        game()


if __name__ == "__main__":
    game()






