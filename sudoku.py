from graph import board, idx_to_coord
from copy import deepcopy
from random import choice
from graph_debug import draw_board, draw_board_domain_lenghts

#returns an array of indices
def get_MRV(inBoard: board): 
    minLen: int = -1
    idx_list = []
    emptyCells = inBoard.get_empty_cells()

    for cell in emptyCells:
        domain = inBoard.domains[cell]
        if minLen == -1 or len(domain) < minLen:
            if(len(domain) >= 0): minLen = len(domain)
    
    for cell in emptyCells:
        currLen = len(inBoard.domains[cell])
        if currLen == minLen:
            idx_list.append(cell)
            
    return idx_list

# returns degree heuristic at a given position (the position must be defined as a tuple)
def get_degree_heuristic(position, inBoard: board) -> int:
    degree = 0
    surrounding = inBoard.get_surrounding_cells(position)
    for point in surrounding:
        lenght = len(inBoard.domains[point])
        if inBoard.values[point] != 0 and lenght >= 1:
            degree += 1
    if degree == 0:
        return degree #just for debugging purposes
    return degree

def fwd_check(inBoard: board, checkAt, value) -> bool:
    # boardToCheck = deepcopy(inBoard)
    if not inBoard.can_be_placed(checkAt[0], checkAt[1], value): 
        return False
    else: 
        inBoard.set_value_at(checkAt[0], checkAt[1], value)

        for domain in inBoard.domains:
            if len(domain) == 0: 
                return False
    
        return True

def solve_sudoku(inBoard: board, depth: int = 0) -> bool:

    if len(inBoard.get_empty_cells()) == 0:
        print("The solution is: ")
        draw_board(inBoard)

    minValues = get_MRV(inBoard)

    maxHeuristicFound = -1
    maxHeurisitcIdx = -1
    for cell in minValues:
        heuristic = inBoard.get_heuristic(cell)
        
        if heuristic > maxHeuristicFound:
            maxHeuristicFound = heuristic
            maxHeurisitcIdx = cell

    # print(maxHeuristicFound)
    idxAsCoord = idx_to_coord(maxHeurisitcIdx)
    valuesToCheck = inBoard.domains[maxHeurisitcIdx].copy()

    boardBefore = deepcopy(inBoard)

    toTraverse = len(valuesToCheck)
    for i in range(toTraverse):
        toCheck = valuesToCheck.pop(0)

        if fwd_check(inBoard, idxAsCoord, toCheck) and solve_sudoku(inBoard):
            return True
        else: inBoard = boardBefore

    return False


