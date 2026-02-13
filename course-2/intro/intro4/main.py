# Make a Tic Tac Toe game using Python
import colorama
from colorama import Fore, Style, init
import random

# Initialize colorama 
init(autoreset=True)

# Create the game board
def display_board(board):
    print()
    def colored(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O":
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(" " + colored(board[0]) + " | " + colored(board[1]) + " | " + colored(board[2]))
    print("-----------")
    print(" " + colored(board[3]) + " | " + colored(board[4]) + " | " + colored(board[5]))
    print("-----------")
    print(" " + colored(board[6]) + " | " + colored(board[7]) + " | " + colored(board[8]))

def pmove(board, symbol):
        move = int(input(Fore.GREEN + "Enter your move (1-9): "))
        if move not in range(1,10):
            print(Fore.RED + "Invalid move. Try again.")
            pmove(board, symbol)
        else:
            board[move-1] = symbol
def ai_move(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return

    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol
            

def check_win(board, symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]             
    ]
    for i in win_conditions:
        if board[i[0]] == board[i[1]] == board[i[2]] == symbol:
            return True
    return False
def check_full(board):
    return all(not spot.isdigit() for spot in board)

def pc():
    symbols = " "
    symbols = input(Fore.GREEN + "Choose your symbol (X/O): ").upper()
    if symbols == "X":
        return "X", "O"
    elif symbols == "O":
        return "O", "X"
def t3():
    print(Fore.CYAN + "Welcome to Tic Tac Toe!")
    name = input(Fore.GREEN + "What's your name? ")
    while True:
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        player_symbol, ai_symbol = pc()
        game_on = True
        turn = "Player"
        if player_symbol == "X":
            turn = "Player"
        else:
            turn = "AI"
        while game_on:
            display_board(board)
            if turn == "Player":
                pmove(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print(Fore.GREEN + f"Congratulations {name}, you win!")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print(Fore.YELLOW + "It's a tie!")
                        game_on = False
                        break
                    turn = "AI"
            elif turn == "AI":
                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print(Fore.RED + "AI wins! Better luck next time.")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print(Fore.YELLOW + "It's a tie!")
                        game_on = False
                        break
                    turn = "Player"
            
if __name__ == "__main__":
    t3()        