from graph import board
from sudoku import solve_sudoku
from graph_debug import draw_board, draw_board_domain_lenghts, draw_board_indeces

testBoard = board()
print(testBoard.can_be_placed(4, 3, 4))
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
draw_board_domain_lenghts(testBoard)

solve_sudoku(testBoard)
# draw_board(testBoard)