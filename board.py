import random
class board:
    # creating the blank board
    int = 6
    board = []
    for i in range(int):
        board.append([])
        for j in range(int):
            board[i].append(0)
    for i in range(int):
        print(board[i])
    # creating board with random pattern
    print("\t")
    newboard = []
    for i in range(int):
        newboard.append([])
        for j in range(int):
          newboard[i].append(random.randrange(0,2))
    for i in range(int):
        print(newboard[i])