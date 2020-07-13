import random
class board:
    # creating the blank board
    int = random.randrange(0,50)
    board = []
    for i in range(int):
        board.append([])
        for j in range(int):
            board[i].append(0)
    for i in range(int):
        print(board[i])
    # creating a random pattern
    print("\t")
    boardindexlist = []
    for i in range(int):
        for j in range(int):
            boardindexlist.append([i, j])
    pattern = random.sample(boardindexlist,4)
    print(pattern)
    board[pattern[0][0]][pattern[0][1]] = 1



    for i in range(int):
        print(board[i])


    """
    print("\t")
    newboard = []
    for i in range(int):
        newboard.append([])
        for j in range(int):
          newboard[i].append(random.randrange(0,2))
    for i in range(int):
        print(newboard[i])
    """