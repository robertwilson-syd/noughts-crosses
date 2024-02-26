import numpy as np
from matplotlib import pyplot
from stl import mesh

def create_board(height, length):
    board = np.zeros((height, length), dtype=int)
    return board


def valid_move(x, y, player, board, n):

    if x >= n:
        print("X value out of bounds.")
        print(f"Please enter a value between 0 and {n - 1} (inclusive)")
        return False
    
    if y >= n:
        print("Y value out of bounds.")
        print(f"Please enter a value between 0 and {n - 1} (inclusive)")
        return False


    if board[y, x] != 0:
        print("Space already taken.")
        return False
    
    board[y,x] = player

    return True

def turn(x, y, player, board, n):    
    if np.all(board[y] == player):
        print(f"Won on horizontal (Row {y})")
        return True

    if np.all(board[:, x] == player):
        print(f"Won on vertical (Column {x})")
        return True

    if x == y:
        diag_arr = board.diagonal()

        if np.all(diag_arr == player):
            print(f"Won on left-to-right diagonal")
            return True        
    
    if x + y == n - 1 :
        anti_diag_arr = np.fliplr(board).diagonal()
        if np.all(anti_diag_arr == player):
            print(f"Won on right-to-left diagonal")
            return True            
    

    return False

def computer(board, player):
    move = [0,0]
    return move

def generate_boards(board, player):
    # list = []
    # list.append(np.zeros((3,3), dtype=int))
    # print(list)
    # darray = np.array(list)
    # print(darray)
    possible_boards = np.empty((1,3,3), dtype=int)
    # possible_boards = np.append(possible_boards, np.zeros((1,3,3), dtype=int), axis=0)
    # print(possible_boards[1])

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i,j] == 0:
                temp_board = np.copy(turn(j, i, player, board))
                possible_boards = np.append(possible_boards, temp_board, axis= 0)
    for a in possible_boards:
        print(a)

def greeting():
    print("Hi welcome to N x N Noughts and Crosses.")
    print("Firstly, choose the dimensions of the board (N must be greater than or equal to 3)")
    n = input("Dimension of the board: ")
    print(f"Thank you we are using an {n} x {n} board you have to get {n}-in-a-row")
    return int(n)

if __name__ == '__main__':
    n = greeting()
    board = create_board(n,n)

    print(board)
    
    
    
    player = 1
    game_over = False
    turn_no = 0

    while not game_over and turn_no < n * n:
        print(f"It is player {player}'s turn.")

        x = int(input("Enter x coordinate (Starts at  0): "))
        y = int(input("Enter y coordinate (Starts at  0): "))

        valid = valid_move(x, y, player, board, n)

        if not valid:
            continue

        game_over = turn(x, y, player, board, n)

        print(board)
        
        if player == 1:
            player = 2
        else:
            player = 1

        turn_no += 1
    
    if game_over == False:
        print("It's a draw.")


    # turn(0, 0, 1, board)
    # generate_boards(board, 1)



