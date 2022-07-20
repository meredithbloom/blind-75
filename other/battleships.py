# m x n matrix where each cell is a battleship 'x' or empty '.'. return number of battleships on board 

# horizontal or vertical only. 
# 1 x k (in a row)
# k x 1 (in a column)
# k can be any size
# at least one vertical/horizontal cell separates battleships (no adjacent battleships)


# brute force:
# iterate through list, left to right, dictionary of ships


# GROUP ADJACENT COORDINATES

from itertools import groupby, product

def distance(tup1, tup2):
    # number of horizontal cells
    x = abs(tup1[0] - tup2[0])
    # number of vertical cells
    y = abs(tup1[1] - tup2[1])
    # we want to find only those pairs where this returns 1 - there is a difference of 1 ONLY vertically OR horizontally
    return x+y


def countBattleships(board):
    pairs = []
    # checking each row
    for x in range(len(board)):
        # checking each column
        for y in range(len(board[0])):
            if board[x][y] == 'X':
                pairs.append((x,y))
    sorted(pairs)
    print(pairs)
    print()
    
    # find every possible pair of pairs
    possible_pairs = product(pairs, repeat = 2)
    # will return list of adjacent tuples
    adjacent = [sorted(pair) for pair in possible_pairs if distance(*pair) == 1]
    print('adjacent tuples are: ' + str(adjacent))
    test_dict = {coordinate: {coordinate} for coordinate in pairs}
    print()
    print(test_dict)
    for tup1, tup2 in adjacent:
        # in-place merge (update) - values at test_dict[tup2] will be added to or overwrite values at test_dict[tup1]
        test_dict[tup1] |= test_dict[tup2]
        # key (coordinate) -> set of all neighboring coordinates, including key
        test_dict[tup2] = test_dict[tup1]
    result = [[*next(val)] for key, val in groupby(sorted(test_dict.values(), key = id), id)]
    print()
    groups = groupby(sorted(test_dict.values(), key=id), id)
    print(test_dict)
    print()
    print(groups)
    print()
    print('sorted dictionary: ' + str(sorted(test_dict.values())))
    print()
    print('grouped elements are: ' + str(result))
    return len(result)

board1 = [["X", ".", ".", "X"], [".", "X", ".", "X"], [".", ".", ".", "X"]]
board2 = [['.']]
countBattleships(board1)





