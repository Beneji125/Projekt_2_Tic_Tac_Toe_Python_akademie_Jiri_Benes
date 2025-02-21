"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jiří Beneš
email: Beneji125@gmail.com
"""

def separator():
    '''
    This function creates a separator.
    '''

    return "=" * 45

def game_introduction():
    '''
    This function prints the game introduction.
    '''

    print(f'''
Welcome to Tic Tac Toe
{separator()}
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
{separator()}
Let's start the game
{separator()} ''')


grid = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
}


def grid_print():
    '''
    This function prints the grid.
    '''

    print(f'''
+---+---+---+
| {grid[1]} | {grid[2]} | {grid[3]} |
+---+---+---+
| {grid[4]} | {grid[5]} | {grid[6]} |
+---+---+---+
| {grid[7]} | {grid[8]} | {grid[9]} |
+---+---+---+
''')


def player_X_turn():
    '''
    This function goes through the player X turn.
    '''

    while True:
        x_choice = input("Player X | Please enter your move number: ")

        if x_choice.isdigit():
            x_choice = int(x_choice)

            if x_choice in grid and grid[x_choice] == " ":
                grid[x_choice] = "X"
                break
            else:
                print("Invalid move! The cell is already occupied or not in range 1 to 9.")
        else:
            print("Invalid input! Please enter a number between 1 and 9.")


def player_O_turn():
    '''
    This function goes through the player O turn.
    '''

    while True:
        o_choice = input("Player O | Please enter your move number: ")

        if o_choice.isdigit():
            o_choice = int(o_choice)

            if o_choice in grid and grid[o_choice] == " ":
                grid[o_choice] = "O"
                break
            else:
                print("Invalid move! The cell is already occupied or not in range 1 to 9.")
        else:
            print("Invalid input! Please enter a number between 1 and 9.")


def win_checker():
    '''
    This function checks if there is a winner.
    '''
    if grid[1] == grid[2] == grid[3] != " ":
        print(f"Player {grid[1]} wins!")
        return True
    elif grid[4] == grid[5] == grid[6] != " ":
        print(f"Player {grid[4]} wins!")
        return True
    elif grid[7] == grid[8] == grid[9] != " ":
        print(f"Player {grid[7]} wins!")
        return True
    elif grid[1] == grid[4] == grid[7] != " ":
        print(f"Player {grid[1]} wins!")
        return True
    elif grid[2] == grid[5] == grid[8] != " ":
        print(f"Player {grid[2]} wins!")
        return True
    elif grid[3] == grid[6] == grid[9] != " ":
        print(f"Player {grid[3]} wins!")
        return True
    elif grid[1] == grid[5] == grid[9] != " ":
        print(f"Player {grid[1]} wins!")
        return True
    elif grid[3] == grid[5] == grid[7] != " ":
        print(f"Player {grid[3]} wins!")
        return True
    elif " " not in grid.values():
        print("It's a draw!")
        return True
    return False


def game_start():
    '''
    This function starts the game.
    '''

    game_introduction()
    win = False
    while win == False:
        grid_print()
        win = win_checker()
        if win == True:
            break
        player_X_turn()
        grid_print()
        win = win_checker()
        if win == True:
            break
        player_O_turn()

game_start()