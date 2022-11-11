from graph import board, idx_to_coord, coord_to_idx
from sudoku import solve_sudoku, get_degree_heuristic, fwd_checking
from graph_debug import draw_board, draw_board_domain_lenghts, draw_board_indeces

testBoard = board()

print(idx_to_coord(1))
print(coord_to_idx(0, 1))
print(testBoard.get_surrounding_cells(10))
# print(get_degree_heuristic(1, testBoard))
# testBoard.set_value_at(0, 0, 4)
# print(get_degree_heuristic(1, testBoard))
