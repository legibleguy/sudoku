from graph import board
from graph_debug import draw_board, draw_board_domain_lenghts

testBoard = board()
testBoard.set_value_at(3, 3, 4)
draw_board(testBoard)