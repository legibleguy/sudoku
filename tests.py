from graph import board, idx_to_coord, coord_to_idx
from sudoku import solve_sudoku, get_degree_heuristic, fwd_checking, get_MRV
from graph_debug import draw_board, draw_board_domain_lenghts, draw_board_indeces

testBoard = board()

testBoard.set_value_at(1,1,5)
draw_board_indeces(testBoard)
draw_board(testBoard)
firstMRV = get_MRV(testBoard)
print("MRV result: " + str(firstMRV))
print("The len of our first MRV run is " + str(len(firstMRV)))


maxHeuristicFound: int = -1
maxHeurisitcIdx: int = -1
for cell in firstMRV:
    heuristic = get_degree_heuristic(cell, testBoard)
    if heuristic > maxHeuristicFound:
        maxHeuristicFound = heuristic
        maxHeurisitcIdx = cell

print("Max Heuristic cell is " + str(maxHeurisitcIdx))
print("The value of the max heuristic is " + str(maxHeuristicFound))

valuesToCheck = testBoard.domains[maxHeurisitcIdx]
currValueToCheck = valuesToCheck.pop(0)

coord = idx_to_coord(maxHeurisitcIdx)
if not testBoard.can_be_placed(coord[0], coord[1], currValueToCheck): pass #return False;
testBoard.set_value_at(coord[0], coord[1], currValueToCheck)
print("we're setting cell #" + str(maxHeurisitcIdx) + " to " + str(currValueToCheck))
draw_board(testBoard)


#the next call of our recursive function
print("After trying to check our first cell, the nbew MRV is " + str(get_MRV(testBoard)))

maxHeuristicFound = -1
maxHeurisitcIdx = -1
for cell in get_MRV(testBoard):
    heuristic = get_degree_heuristic(cell, testBoard)
    if heuristic > maxHeuristicFound:
        maxHeuristicFound = heuristic
        maxHeurisitcIdx = cell

print("Max Heuristic cell is " + str(maxHeurisitcIdx))
print("The value of the max heuristic is " + str(maxHeuristicFound))

valuesToCheck2 = testBoard.domains[maxHeurisitcIdx]
currValueToCheck2 = valuesToCheck2.pop(0)

coord = idx_to_coord(maxHeurisitcIdx)
testBoard.set_value_at(coord[0], coord[1], currValueToCheck2)
print("we're setting cell #" + str(maxHeurisitcIdx) + " to " + str(currValueToCheck2))
draw_board(testBoard)

# print(get_degree_heuristic(1, testBoard))
# testBoard.set_value_at(0, 0, 4)
# print(get_degree_heuristic(1, testBoard))
