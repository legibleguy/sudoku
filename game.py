from graph import board, idx_to_coord
from sudoku import *
from graph_debug import draw_board, draw_board_domain_lengths, draw_board_indices
import time

firstBoard = board()
secondBoard = board()
thirdBoard = board()

#First Board
firstBoard.set_value_at(0, 2, 1)
firstBoard.set_value_at(0, 5, 2)
firstBoard.set_value_at(1, 2, 5)
firstBoard.set_value_at(1, 5, 6)
firstBoard.set_value_at(1, 7, 3)
firstBoard.set_value_at(2, 0, 4)
firstBoard.set_value_at(2, 1, 6)
firstBoard.set_value_at(2, 5, 5)

firstBoard.set_value_at(3, 3, 1)
firstBoard.set_value_at(3, 5, 4)
firstBoard.set_value_at(4, 0, 6)
firstBoard.set_value_at(4, 3, 8)
firstBoard.set_value_at(4, 6, 1)
firstBoard.set_value_at(4, 7, 4)
firstBoard.set_value_at(4, 8, 3)
firstBoard.set_value_at(5, 4, 9)
firstBoard.set_value_at(5, 6, 5)
firstBoard.set_value_at(5, 8, 8)

firstBoard.set_value_at(6, 0, 8)
firstBoard.set_value_at(6, 4, 4)
firstBoard.set_value_at(6, 5, 9)
firstBoard.set_value_at(6, 7, 5)
firstBoard.set_value_at(7, 0, 1)
firstBoard.set_value_at(7, 3, 3)
firstBoard.set_value_at(7, 4, 2)
firstBoard.set_value_at(8, 2, 9)
firstBoard.set_value_at(8, 6, 3)

#Second Board
secondBoard.set_value_at(0, 2, 5)
secondBoard.set_value_at(0, 4, 1)
secondBoard.set_value_at(1, 2, 2)
secondBoard.set_value_at(1, 5, 4)
secondBoard.set_value_at(1, 7, 3)
secondBoard.set_value_at(2, 0, 1)
secondBoard.set_value_at(2, 2, 9)
secondBoard.set_value_at(2, 6, 2)
secondBoard.set_value_at(2, 8, 6)

secondBoard.set_value_at(3, 0, 2)
secondBoard.set_value_at(3, 4, 3)
secondBoard.set_value_at(4, 1, 4)
secondBoard.set_value_at(4, 6, 7)
secondBoard.set_value_at(5, 0, 5)
secondBoard.set_value_at(5, 5, 7)
secondBoard.set_value_at(5, 8, 1)

secondBoard.set_value_at(6, 3, 6)
secondBoard.set_value_at(6, 5, 3)
secondBoard.set_value_at(7, 1, 6)
secondBoard.set_value_at(7, 3, 1)
secondBoard.set_value_at(8, 4, 7)
secondBoard.set_value_at(8, 7, 5)

#Third Board
thirdBoard.set_value_at(0, 0, 6)
thirdBoard.set_value_at(0, 1, 7)
thirdBoard.set_value_at(1, 1, 2)
thirdBoard.set_value_at(1, 2, 5)
thirdBoard.set_value_at(2, 1, 9)
thirdBoard.set_value_at(2, 3, 5)
thirdBoard.set_value_at(2, 4, 6)
thirdBoard.set_value_at(2, 6, 2)

thirdBoard.set_value_at(3, 0, 3)
thirdBoard.set_value_at(3, 4, 8)
thirdBoard.set_value_at(3, 6, 9)
thirdBoard.set_value_at(4, 6, 8)
thirdBoard.set_value_at(4, 8, 1)
thirdBoard.set_value_at(5, 3, 4)
thirdBoard.set_value_at(5, 4, 7)

thirdBoard.set_value_at(6, 2, 8)
thirdBoard.set_value_at(6, 3, 6)
thirdBoard.set_value_at(6, 7, 9)
thirdBoard.set_value_at(7, 7, 1)
thirdBoard.set_value_at(8, 0, 1)
thirdBoard.set_value_at(8, 2, 6)
thirdBoard.set_value_at(8, 4, 5)
thirdBoard.set_value_at(8, 7, 7)

#Solve the first instance
start_instance1 = time.process_time()
print("First Board before solution")
draw_board(firstBoard)
solve_sudoku(firstBoard)
end_instance1 = time.process_time()
print("First Board took " + str(end_instance1 - start_instance1) + " CPU execution time to complete.")
print ("\n")


#Solve the second instance
start_instance2 = time.process_time()
print("Second Board before solution")
draw_board(secondBoard)
solve_sudoku(secondBoard)
end_instance2 = time.process_time()
print("Second Board took " + str(end_instance2 - start_instance2) + " CPU execution time to complete.")
print ("\n")


#Solve the third instance
start_instance3 = time.process_time()
print("Third Board before solution")
draw_board(thirdBoard)
solve_sudoku(thirdBoard)
end_instance3 = time.process_time()
print("Third Board took " + str(end_instance3 - start_instance3) + " CPU execution time to complete.")
print ("\n")
