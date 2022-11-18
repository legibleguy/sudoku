from graph import board, idx_to_coord, coord_to_idx
from sudoku import solve_sudoku, get_degree_heuristic, fwd_check, get_MRV
from graph_debug import draw_board, draw_board_domain_lenghts, draw_board_indeces

testBoard = board()

testBoard.set_value_at(1,1, 3)
testBoard.set_value_at(1,3, 4)
testBoard.set_value_at(2,2, 5)

draw_board(testBoard)

print(fwd_check(testBoard, [1, 2], 3))
draw_board(testBoard)
