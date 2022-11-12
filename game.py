from graph import board, idx_to_coord
from sudoku import *
from graph_debug import draw_board, draw_board_domain_lenghts, draw_board_indeces

testBoard = board()
#print(testBoard.can_be_placed(4, 3, 4))
testBoard.set_value_at(0, 0, 5)
testBoard.set_value_at(0, 1, 6)
testBoard.set_value_at(1, 0, 3)
testBoard.set_value_at(1, 2, 9)
testBoard.set_value_at(4, 0, 7)
testBoard.set_value_at(3, 1, 1)
testBoard.set_value_at(4, 1, 9)
testBoard.set_value_at(5, 1, 5)
# testBoard.set_value_at(2, 2, 9)
testBoard.set_value_at(2, 2, 8)
testBoard.set_value_at(7, 2, 6)

testBoard.set_value_at(0, 3, 8)
testBoard.set_value_at(0, 4, 4)
testBoard.set_value_at(0, 5, 7)
testBoard.set_value_at(4, 3, 6)
testBoard.set_value_at(3, 4, 8)
testBoard.set_value_at(5, 4, 3)
testBoard.set_value_at(4, 5, 2)
testBoard.set_value_at(8, 3, 3)
testBoard.set_value_at(8, 4, 1)
testBoard.set_value_at(8, 5, 6)

testBoard.set_value_at(1, 6, 6)
testBoard.set_value_at(3, 7, 4)
testBoard.set_value_at(4, 7, 1)
testBoard.set_value_at(5, 7, 9)
testBoard.set_value_at(4, 8, 8)
testBoard.set_value_at(6, 6, 2)
testBoard.set_value_at(7, 6, 8)
testBoard.set_value_at(8, 7, 5)
testBoard.set_value_at(7, 8, 7)
testBoard.set_value_at(8, 8, 9)

draw_board(testBoard)
# draw_board_domain_lenghts(testBoard)
# draw_board_indeces(testBoard)

##TO REMOVE

# print("MRV result: " + str(get_MRV(testBoard)))
# print("domain size at cell #40 is " + str(len(testBoard.domains[40])))
# print("the domain at cell #40 is " + str(testBoard.domains[40]))
# print("domain size at cell #51 is " + str(len(testBoard.domains[51])))
# print("the domain at cell #51 is " + str(testBoard.domains[51]))
# print("domain size at cell #70 is " + str(len(testBoard.domains[70])))
# print("the domain at cell #70 is " + str(testBoard.domains[70]))
# print("domain size at cell #78 is " + str(len(testBoard.domains[78])))
# print("the domain at cell #78 is " + str(testBoard.domains[78]))

# maxHeuristicFound: int = -1
# maxHeurisitcIdx: int = -1

# firstMRV = get_MRV(testBoard)

# for cell in firstMRV:
#         heuristic = get_degree_heuristic(cell, testBoard)
#         if heuristic > maxHeuristicFound:
#             maxHeuristicFound = heuristic
#             maxHeurisitcIdx = cell

# print("the index of the max heuristic" + str(maxHeurisitcIdx))
# print("the value of the max heuristic" + str(maxHeuristicFound))

# coords = idx_to_coord(get_MRV(testBoard)[0])
# print("Setting the value in the cell that has only one possible cvalue left (" + str(coords) + ")")
# testBoard.set_value_at(coords[0], coords[1], testBoard.domains[40][0])

# for cell in firstMRV:
#     coord = idx_to_coord(cell)
#     testBoard.set_value_at(coord[0], coord[1], testBoard.domains[cell][0])

# print("After setting values in 4 cells our MRV is " + str(get_MRV(testBoard)))
# print("The lenght of the new MRV is " + str(len(testBoard.domains[get_MRV(testBoard)[0]])))

##

solve_sudoku(testBoard)
draw_board(testBoard)
# draw_board(testBoard)