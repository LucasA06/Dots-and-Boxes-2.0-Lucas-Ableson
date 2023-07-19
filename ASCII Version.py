import random

# Grid settings
grid_size = 4
grid_range = 3
grid_range2 = 4

# Create an empty grid
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

# Initialize players
players = ['P1', 'P2']
current_player = random.choice(players)

# Function to display the grid
def display_grid():
    print('+' + '---+' * grid_size)
    for row in grid:
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print('\n+' + '---+' * grid_size)

# Function to check if the grid is full
def is_grid_full():
    for row in grid:
        if ' ' in row:
            return False
    return True

# Function to check if a player has won
def is_winner(player):
    # Check rows
    for row in grid:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(grid_size):
        if all(grid[row][col] == player for row in range(grid_size)):
            return True

    # Check diagonals
    if all(grid[i][i] == player for i in range(grid_size)):
        return True

    if all(grid[i][grid_size - 1 - i] == player for i in range(grid_size)):
        return True

    return False

# Function to make a move
def make_move(player, row, col):
    if grid[row][col] == ' ':
        grid[row][col] = player
        return True
    return False

# Function to switch players
def switch_players():
    global current_player
    if current_player == players[0]:
        current_player = players[1]
    else:
        current_player = players[0]

# Function to start the game
def start_game():
    while not is_grid_full():
        display_grid()

        print(f"\n{current_player}'s Turn")
        row = int(input("Enter the row number 0-3): "))
        col = int(input("Enter the column number (0-3): "))

        if row in range(grid_size) and col in range(grid_size):
            if make_move(current_player, row, col):
                if is_winner(current_player):
                    display_grid()
                    print(f"\n{current_player} wins!")
                    break
                switch_players()
            else:
                print("Invalid move. Try again.")
        else:
            print("Invalid row or column number. Try again.")

    if is_grid_full():
        display_grid()
        print("\nIt's a tie!")

# Start the game
start_game()
