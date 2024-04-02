from os import system, name

# Constants:
BOARD_SIZE = 3 # must be a positive integer
FIRST_CHAR = 'X' # as long both are unique and not ' '
SECND_CHAR = 'O'

# Custom Exceptions
class OccupiedSquareError(Exception):
  """Exception for indicating that the selected square is already occupied."""
  pass

# Helper Functions:
def clear():
    '''
    Purpose:
      clear output to remove clutter
    Parameters:
      None
    Returns:
      None
    Time:
      O(1)
    '''
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')

def board_make():
  '''
  Purpose: 
    returns a BOARD_SIZE x BOARD_SIZE list filled with ' '
  Parameters:
    None
  Returns:
    board: STR[BOARD_SIZE][BOARD_SIZE]
  Time:
    O(n^2), n = BOARD_SIZE
  '''
  board = []
  for r in range(0, BOARD_SIZE):
    row = []
    for c in range(0, BOARD_SIZE):
      row.append(' ')
    board.append(row)
  return board

def board_print(board):
  '''
  Purpose:
    prints the tic-tac-toe board
  Parameters:
    board: STR[BOARD_SIZE][BOARD_SIZE]
  Returns:
    None
  Effects:
    prints to output
  Time:
    O(n^2), n = BOARD_SIZE
  '''
  clear()
  for r in range(BOARD_SIZE):
    to_print = ""
    for c in range(BOARD_SIZE):
      if c < BOARD_SIZE - 1:
        to_print += " {} |".format(board[r][c])
      else:
        to_print += " {}\n".format(board[r][c])
    
    if r < BOARD_SIZE - 1:
      for c in range(BOARD_SIZE):
        to_print += "---"
        if c < BOARD_SIZE - 1:
          to_print += "+"
    print(to_print)

def check_rows(board) -> int:
  '''
  Purpose:
    checks all rows for one that is filled with either
    FIRST_CHAR ('X') -> 1 or SECND_CHAR ('O') -> 2
    or if there are no such rows -> 0
  Parameters:
    board: STR[BOARD_SIZE][BOARD_SIZE]
  Returns:
    anyof{0, 1, 2}
  Time:
    O(n^2), n = BOARD_SIZE
  '''
  for r in range(BOARD_SIZE):
    first = board[r][0]
    if first == ' ': continue
    for c in range(BOARD_SIZE):
      if board[r][c] != first:
        break
      elif c == BOARD_SIZE - 1:
        return 1 if first == FIRST_CHAR else 2
  return 0

def check_cols(board) -> int:
  '''
  Purpose:
    checks all columns for one that is filled with either
    FIRST_CHAR ('X') -> 1 or SECND_CHAR ('O') -> 2
    or if there are no such columns -> 0
  Parameters:
    board: STR[BOARD_SIZE][BOARD_SIZE]
  Returns:
    anyof{0, 1, 2}
  Time:
    O(n^2), n = BOARD_SIZE
  '''
  for c in range(BOARD_SIZE):
    first = board[0][c]
    if first == ' ': continue
    for r in range(BOARD_SIZE):
      if board[r][c] != first:
        break
      elif r == BOARD_SIZE - 1:
        return 1 if first == FIRST_CHAR else 2
  return 0

def check_dias(board) -> int:
  '''
  Purpose:
    checks all diagonals for one that is filled with either
    FIRST_CHAR ('X') -> 1 or SECND_CHAR ('O') -> 2
    or if there are no such diagonals -> 0
  Parameters:
    board: STR[BOARD_SIZE][BOARD_SIZE]
  Returns:
    anyof{0, 1, 2}
  Time:
    O(n), n = BOARD_SIZE
  '''
  first = board[0][0]
  if first != ' ':
    for i in range(BOARD_SIZE):
      if board[i][i] != first:
        break
      elif i == BOARD_SIZE - 1:
        return 1 if first == FIRST_CHAR else 2
      
  first = board[0][BOARD_SIZE - 1]
  if first != ' ':
    for j in range(BOARD_SIZE):
      if board[j][BOARD_SIZE - j - 1] != first:
        break
      elif j == BOARD_SIZE - 1:
        return 1 if first == FIRST_CHAR else 2
  return 0

def check_winner(board, turns) -> int:
  '''
  Purpose:
    checks if there is a winner (1/2), a draw (3), or nothing yet (0)
  Parameters:
    board: STR[BOARD_SIZE][BOARD_SIZE]
    turns: int
  Returns:
    anyof{0, 1, 2, 3}
  Time:
    O(n^2), n = BOARD_SIZE
  '''
  rows = check_rows(board) # O(n^2)
  if rows != 0: return rows

  cols = check_cols(board) # O(n^2)
  if cols != 0: return cols

  dias = check_dias(board) # O(n)
  if dias != 0: return dias

  if turns >= BOARD_SIZE * BOARD_SIZE: return 3

  return 0

def is_valid(board, move) -> bool:
  '''
  Purpose:
    checks if a given move is possible
  Parameters:
    board: STR[BOARD_SIZE][BOARD_SIZE]
    move: [int, int]
  Returns:
    bool
  Time:
    O(1)
  '''
  if move[0] < 0 or move[0] >= BOARD_SIZE:
    return False
  elif move[1] < 0 or move[1] >= BOARD_SIZE:
    return False
  else:
    return (board[move[0]][move[1]] == ' ')

def get_move(board, turns):
  '''
  Purpose:
    asks a user for their move then checks if it's valid. if it is, returns it
  Parameters:
    board: STR[BOARD_SIZE][BOARD_SIZE]
    turns: int
  Returns:
    [anyof{1, ..., BOARD_SIZE}, anyof{1, ..., BOARD_SIZE}], row and column of move
  Time:
    O(1)
  '''
  move_row, move_col = 0, 0
  while (move_row == 0 and move_col == 0):
    board_print(board)
    print("It is now {}'s turn.".format(name1 if turns % 2 == 0 else name2))
    print("Enter your moves as: ROW COLUMN (0 - {})".format(BOARD_SIZE - 1))

    try:
      row, col = input().strip().split()
      row = int(row)
      col = int(col) # Possible ValueError

      if is_valid(board, [row, col]):
        move_row = row
        move_col = col
        break
      else:
        raise OccupiedSquareError
    except ValueError:
      print("This is not valid input. Please enter two INTEGERS from 0 to {}, separated by a space".format(BOARD_SIZE - 1))
      input("Press Enter to continue...")
    except IndexError:
      print("This is not valid input. Please enter TWO integers from 0 to {}, separated by a space".format(BOARD_SIZE - 1))
      input("Press Enter to continue...")
    except OccupiedSquareError:
      print("This is not a valid move. Please enter another pair of integers from 0 to {}, separated by a space".format(BOARD_SIZE - 1))
      input("Press Enter to continue...")
  return move_row, move_col

def play_round(name1, name2) -> bool:
  '''
  Purpose:
    the game loop, keeps repeating until winner or stop playing
  Parameters:
    name1: str
    name2: str
  Returns:
    bool
  Time:
    O(n^2), n = BOARD_SIZE
  '''
  board = board_make()
  turns_played = 0

  while turns_played < (BOARD_SIZE * BOARD_SIZE):
    move_row, move_col = get_move(board, turns_played)
    board[move_row][move_col] = FIRST_CHAR if turns_played % 2 == 0 else SECND_CHAR
    turns_played += 1

    win = check_winner(board, turns_played)
    if win == 0:
      continue
    elif win == 1:
      board_print(board)
      print("{} has WON! Congratulations!".format(name1))
      break
    elif win == 2:
      board_print(board)
      print("{} has WON! Congratulations!".format(name2))
      break
    elif win == 3:
      board_print(board)
      print("All squares have been filled, and the game ends in a draw!")
      break
    
  print('If you would like a rematch, please enter "yes"')
  print("Otherwise, enter anything else.")
  return input().lower() == "yes"

# MAIN:
# Getting basic info:
print("Welcome to Tic Tac Toe!")
name1 = input("Player 1 ({}), please enter your name: ".format(FIRST_CHAR)).strip()
name2 = input("Player 2 ({}), please enter your name: ".format(SECND_CHAR)).strip()
print("Welcome {} and {}! We hope you enjoy playing!".format(name1, name2))

input("Press Enter to continue...")
clear()

# Actual Gameplay
while (play_round(name1, name2)):
  continue
clear()
print("Thank you for playing!")
