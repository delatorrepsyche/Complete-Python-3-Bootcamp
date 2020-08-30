# Print the board
# Ask the Player 1 for his symbol (X or O)
# Start Game
# Ask players for position
# Check if someone won
# If someone won then ask the players if they want to play again
# Else end the game
from IPython.display import clear_output
import sys
import os

board = [' '] * 9
player1_mark = ''
player2_mark = ''


def introduction_msg():
    print("\n\nHi there! Welcome to this simple tic tac toe game.")
    while True:
        player_answer = input("Do you want to play? [Y/N]: ")
        if player_answer.lower() == 'y':
            clear_output()
            return True
        elif player_answer.lower() == 'n':
            return False
        else:
            print("(Please select either Y or N)")


def display_rules():
    print("\n---------------------------")
    print("Great! The rule is simple!")
    print("---------------------------")
    print("The first one who can make a")
    print("horizontal/vertical/diagonal")
    print("with their chosen symbol wins!")
    print("Good luck!")
    print("---------------------------\n")


def display_board():
    clear_output()
    print("Let's start!")
    for slot in range(0, len(board)):
        if (slot + 1) % 3 == 0 and (slot + 1) != 9:
            sys.stdout.write(board[slot] + "\n")
        else:
            sys.stdout.write(board[slot])
            if (slot + 1) == 9:
                sys.stdout.write("\b")
            else:
                sys.stdout.write("|")
            sys.stdout.flush()
    return True


def ask_player_symbol():
    while True:
        player_symbol = input("Please select a mark Player1 [X/O]: ")
        if player_symbol.lower() == 'x':
            player1_mark = 'X'
            player2_mark = 'O'
            break
        elif player_symbol.lower() == 'o':
            player1_mark = 'O'
            player2_mark = 'X'
            break
        else:
            print("Invalid input!\n")
    print("PLAYER 1 will be " + player1_mark)
    print("PLAYER 2 will be " + player2_mark)
    input("Press Enter to continue...")
    clear_output()
    return (player1_mark, player2_mark)


def set_position(player_pos, player_mark):
    position_invalid = False
    if board[player_pos - 1] == ' ':
        board[player_pos - 1] = player_mark
        os.system('cls')
        display_board()
    else:
        print('The selected slot already has a value.')
        position_invalid = True
    return position_invalid


def board_has_space():
    has_space = False
    for count in range(0, len(board)):
        if board[count] == ' ':
            has_space = True
            break
        else:
            pass
    return has_space


def check_winner():
    if board[0] == board[1] == board[2] and board[0] != ' ':
        return True
    elif board[3] == board[4] == board[5] and board[3] != ' ':
        return True
    elif board[6] == board[7] == board[8] and board[6] != ' ':
        return True
    elif board[0] == board[3] == board[6] and board[0] != ' ':
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        return True
    elif board[0] == board[4] == board[8] and board[0] != ' ':
        return True
    elif board[2] == board[4] == board[6] and board[2] != ' ':
        return True
    else:
        return False


def game_on(player1_mark, player2_mark):
    player = 'Player 1'
    is_invalid_pos = False
    display_board()
    while True:
        print("")
        while True:
            position = input(f"{player} please select a number from 1-9: ")
            if position.isdigit() is True:
                position = int(position)
                if position >= 1 and position <= 9:
                    break
                elif position < 1 or position > 9:
                    print('Out of range!')
            elif position.isdigit() is False:
                print("Invalid input!")
        if player == 'Player 1':
            is_invalid_pos = set_position(position, player1_mark)
        else:
            is_invalid_pos = set_position(position, player2_mark)
        if board_has_space() is False and check_winner() is False:
            return 'draw'
        if check_winner():
            return player

        if is_invalid_pos is False:
            if player == 'Player 1':
                player = 'Player 2'
            else:
                player = 'Player 1'


isplaying = introduction_msg()
if isplaying is True:
    display_rules()
    (player_1, player_2) = ask_player_symbol()
    display_board()
    os.system('cls')
    winner = game_on(player_1, player_2)
    if winner == 'draw':
        print("\nIt's a draw!")
    else:
        print(f"\nWinner is {winner}!")
else:
    print("That's sad :(")