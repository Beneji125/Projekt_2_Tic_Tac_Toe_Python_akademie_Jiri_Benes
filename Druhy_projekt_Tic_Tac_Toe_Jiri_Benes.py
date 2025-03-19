"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jiří Beneš
email: Beneji125@gmail.com
"""


def separator():
    '''
    This function creates a separator to make the code output 
    more readable and easier to follow.
    '''
        
    return "=" * 90

def game_introduction():
    '''
    This function prints the game introduction 
    and explains the rules of TIC-TAC-TOE.
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

def grid_print(grid):
    '''
    This function prints the grid of the game, 
    so the players can see the current state of the game.
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

def win_checker(grid, player):
    '''
    This function checks if there are three same symbols in a line and if yes,
    declares a winner. If not, it checks if the grid is full and if yes,
    declares a draw. Otherwise, it continues the game.
    '''

    if (grid[1] == grid[2] == grid[3] != " " 
        or grid[4] == grid[5] == grid[6] != " "
        or grid[7] == grid[8] == grid[9] != " "
        or grid[1] == grid[4] == grid[7] != " "
        or grid[2] == grid[5] == grid[8] != " "
        or grid[3] == grid[6] == grid[9] != " "
        or grid[1] == grid[5] == grid[9] != " "
        or grid[3] == grid[5] == grid[7] != " "):
        grid_print(grid)
        print(separator())
        print(f"Congratulations player {player} wins!")
        print(separator())
        return True
    elif " " not in grid.values():
        grid_print(grid)
        print(separator()) 
        print("It's a draw!")
        print(separator()) 
        return True
    return False

def player_turn(grid, player):
    '''
    This function goes through the players' turns, alternating between player X
    and player O. It also checks if there is a winner or a draw using the 
    win_checker function. There is also an option to quit the game if needed.
    '''
        
    while True:
        if win_checker(grid, player): 
            return  

        player = "O" if player == "X" else "X"
        print(separator())
        print(f"Player {player}'s turn")
        grid_print(grid)

        while True: 
            player_choice = input(f"Player {player} | Enter a number (1-9) or 'q' to quit: ").strip().lower()

            if player_choice in ["q", "quit"]:
                print(separator())
                print("Game Over. A player has quit.")
                print(separator())
                return  

            elif player_choice.isdigit():
                player_choice = int(player_choice)

                if player_choice in grid and grid[player_choice] == " ":
                    grid[player_choice] = player
                    print(separator())  
                    break  
                else:
                    print("Invalid move! The cell is already occupied or not in range 1 to 9.")
            else:
                print("Invalid input! Please enter a number between 1 and 9, or 'q' to quit.")

def game_start():
    '''
    This function contains and starts the game of TIC-TAC-TOE 
    by calling on other functions.
    '''
        
    game_introduction()
    grid = {
        1: " ", 2: " ", 3: " ",
        4: " ", 5: " ", 6: " ",
        7: " ", 8: " ", 9: " "
    }
    player = "O"
    player_turn(grid, player)


if __name__ == "__main__":
    game_start()