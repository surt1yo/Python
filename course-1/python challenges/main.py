#Write a Python Program to create a Tic Tac Toe game. 
#You can use different modules and functions to create this game. 
#Make sure that you print the board after every move.
theBoard={'7':' ','8':' ','9':' ',
          '4':' ','5':' ','6':' ',
          '1':' ','2':' ','3':' '}
board_keys=[]
def print_board(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['1']+'|'+board['2']+'|'+board['3'])
def game():
    turn='X'
    count=0
    for i in range(9):
        print_board(theBoard)
        print(f"{turn}'s turn. Move to which place?")
        move=input()
        if theBoard[move]==' ':
            theBoard[move]=turn
            count+=1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        if count>=5:
            #checking the top row
            if theBoard['7']==theBoard['8']==theBoard['9']!=' ':
                print_board(theBoard)
                print(f"Game Over.\n{turn} wins!")
                break
            elif theBoard['4']==theBoard['5']==theBoard['6']!=' ':
                print_board(theBoard)
                print(f"Game Over.\n{turn} wins!")
                break
            elif theBoard['1']==theBoard['2']==theBoard['3']!=' ':
                print_board(theBoard)
                print(f"Game Over.\n{turn} wins!")
                break
            elif theBoard['7']==theBoard['4']==theBoard['1']!=' ':
                print_board(theBoard)
                print(f"Game Over.\n{turn} wins!")
                break
            elif theBoard['8']==theBoard['5']==theBoard['2']!=' ':
                print_board(theBoard)
                print(f"Game Over.\n{turn} wins!")
                break
            elif theBoard['9']==theBoard['6']==theBoard['3']!=' ':
                print_board(theBoard)
                print(f"Game Over.\n{turn} wins!")
                break
            elif theBoard['7']==theBoard['5']==theBoard['3']!=' ':
                print_board(theBoard)
                print(f"Game Over.\n{turn} wins!")
                break
            elif theBoard['9']==theBoard['5']==theBoard['1']!=' ':
                print_board(theBoard)
                print(f"Game Over.\n{turn} wins!")
                break
            else:
                if count==9:
                    print("Game Over.\nIt's a Tie!")
        if turn=='X':
            turn='O'    
        else:
            turn='X'
game()
 