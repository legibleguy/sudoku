from graph import board, idx_to_coord
from sudoku import *
from graph_debug import draw_board, draw_board_domain_lenghts, draw_board_indeces
import time

testBoard = board()
firstBoard = board()
secondBoard = board()
thirdBoard = board()

#print(testBoard.can_be_placed(4, 3, 4))
# testBoard.set_value_at(0, 0, 5)
# testBoard.set_value_at(0, 1, 6)
# testBoard.set_value_at(1, 0, 3)
# testBoard.set_value_at(1, 2, 9)
# testBoard.set_value_at(4, 0, 7)
# testBoard.set_value_at(3, 1, 1)
# testBoard.set_value_at(4, 1, 9)
# testBoard.set_value_at(5, 1, 5)
# # testBoard.set_value_at(2, 2, 9)
# testBoard.set_value_at(2, 2, 8)
# testBoard.set_value_at(7, 2, 6)

# testBoard.set_value_at(0, 3, 8)
# testBoard.set_value_at(0, 4, 4)
# testBoard.set_value_at(0, 5, 7)
# testBoard.set_value_at(4, 3, 6)
# testBoard.set_value_at(3, 4, 8)
# testBoard.set_value_at(5, 4, 3)
# testBoard.set_value_at(4, 5, 2)
# testBoard.set_value_at(8, 3, 3)
# testBoard.set_value_at(8, 4, 1)
# testBoard.set_value_at(8, 5, 6)

# testBoard.set_value_at(1, 6, 6)
# testBoard.set_value_at(3, 7, 4)
# testBoard.set_value_at(4, 7, 1)
# testBoard.set_value_at(5, 7, 9)
# testBoard.set_value_at(4, 8, 8)
# testBoard.set_value_at(6, 6, 2)
# testBoard.set_value_at(7, 6, 8)
# testBoard.set_value_at(8, 7, 5)
# testBoard.set_value_at(7, 8, 7)
# testBoard.set_value_at(8, 8, 9)

#board based on example from first meeting
# testBoard.set_value_at(0, 0, 5)
# testBoard.set_value_at(0, 1, 3)
# testBoard.set_value_at(1, 0, 6)
# testBoard.set_value_at(2, 1, 9)
# testBoard.set_value_at(2, 2, 8)
# testBoard.set_value_at(0, 4, 7)
# testBoard.set_value_at(1, 3, 1)
# testBoard.set_value_at(1, 4, 9)
# testBoard.set_value_at(1, 5, 5)
# testBoard.set_value_at(2, 7, 6)

# testBoard.set_value_at(3, 0, 8)
# testBoard.set_value_at(4, 0, 4)
# testBoard.set_value_at(5, 0, 7)
# testBoard.set_value_at(3, 4, 6)
# testBoard.set_value_at(4, 3, 8)
# testBoard.set_value_at(4, 5, 3)
# testBoard.set_value_at(5, 4, 2)
# testBoard.set_value_at(3, 8, 3)
# testBoard.set_value_at(4, 8, 1)
# testBoard.set_value_at(5, 8, 6)

# testBoard.set_value_at(6, 1, 6)
# testBoard.set_value_at(6, 6, 2)
# testBoard.set_value_at(6, 7, 8)
# testBoard.set_value_at(7, 3, 4)
# testBoard.set_value_at(7, 4, 1)
# testBoard.set_value_at(7, 5, 9)
# testBoard.set_value_at(7, 8, 5)
# testBoard.set_value_at(8, 4, 8)
# testBoard.set_value_at(8, 7, 7)
# testBoard.set_value_at(8, 8, 9)

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

# print("First Board before solution")
# draw_board(firstBoard)
# print("Second Board before solution")
# draw_board(secondBoard)
# print("Third Board before solution")
# draw_board(thirdBoard)

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

#Solve the first instance
start_instance1 = time.process_time()
print("First Board before solution")
draw_board(firstBoard)
solve_sudoku(firstBoard)
print("Solution for First Board is")
draw_board(firstBoard)
end_instance1 = time.process_time()
print("First Board took " + str(end_instance1 - start_instance1) + " CPU execution time to complete.")
print ("\n")


#Solve the second instance
start_instance2 = time.process_time()
print("Second Board before solution")
draw_board(secondBoard)
solve_sudoku(secondBoard)
print("Solution for Second Board is")
draw_board(secondBoard)
end_instance2 = time.process_time()
print("Second Board took " + str(end_instance2 - start_instance2) + " CPU execution time to complete.")
print ("\n")


#Solve the third instance
start_instance3 = time.process_time()
print("Third Board before solution")
draw_board(thirdBoard)
solve_sudoku(thirdBoard)
print("Solution for Third Board is")
draw_board(thirdBoard)
end_instance3 = time.process_time()
print("Third Board took " + str(end_instance3 - start_instance3) + " CPU execution time to complete.")
print ("\n")

#draw_board(testBoard)
# draw_board(testBoard)