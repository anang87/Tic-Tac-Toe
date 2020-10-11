# Tic Tac Toe In The Console

# Create an empty list for used numbers
used_numbers = []

# Create the gameboard spots as a dictionary
gameboard = {1: '1', 2: '2', 3: '3',
             4: '4', 5: '5', 6: '6',
             7: '7', 8: '8', 9: '9'}

# Define a function to show the gameboard like in the real Tic Tac Toe
def show_gameboard():
    print("")
    print(gameboard[1] + ' | ' + gameboard[2] + ' | ' + gameboard[3])
    print('--+---+--')
    print(gameboard[4] + ' | ' + gameboard[5] + ' | ' + gameboard[6])
    print('--+---+--')
    print(gameboard[7] + ' | ' + gameboard[8] + ' | ' + gameboard[9])

# Define X's turn as a function
def X_turn():
    X_input = int(input("Where do you want to place X? Choose a number on the board.\n"))
    if X_input in used_numbers:
        print("That position is full, try another one\n")
        X_turn()
    elif X_input not in gameboard:
        print("Invalid Position")
        X_turn()
    used_numbers.append(X_input)
    gameboard[X_input] = 'X'

# Define O's turn as a function
def O_turn():
    O_input = int(input("Where do want to place O? Choose a number on the board.\n"))
    if O_input in used_numbers:
        print("That position is full, try another one\n")
        O_turn()
    used_numbers.append(O_input)
    gameboard[O_input] = 'O'

# Define the actual gameplay function
def gameplay():
    for i in range(9):
        show_gameboard()
        X_turn()
        if len(used_numbers) == 9:
            print("Game over, it's a tie\n")
            break
        elif gameboard[1] == gameboard[2] == gameboard[3] or \
           gameboard[4] == gameboard[5] == gameboard[6] or \
           gameboard[7] == gameboard[8] == gameboard[9] or \
           gameboard[1] == gameboard[4] == gameboard[7] or \
           gameboard[2] == gameboard[5] == gameboard[8] or \
           gameboard[3] == gameboard[6] == gameboard[9] or \
           gameboard[1] == gameboard[5] == gameboard[9] or \
           gameboard[3] == gameboard[5] == gameboard[7]:
           show_gameboard()
           print("Game over, X wins\n")
           break

        show_gameboard()
        O_turn()
        if len(used_numbers) == 9:
            show_gameboard()
            print("Game over, it's a tie\n")
            break
        elif gameboard[1] == gameboard[2] == gameboard[3] or \
           gameboard[4] == gameboard[5] == gameboard[6] or \
           gameboard[7] == gameboard[8] == gameboard[9] or \
           gameboard[1] == gameboard[4] == gameboard[7] or \
           gameboard[2] == gameboard[5] == gameboard[8] or \
           gameboard[3] == gameboard[6] == gameboard[9] or \
           gameboard[1] == gameboard[5] == gameboard[9] or \
           gameboard[3] == gameboard[5] == gameboard[7]:
           show_gameboard()
           print("Game over, O wins\n")
           break

gameplay()