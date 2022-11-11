from graph import board, idx_to_coord
from copy import deepcopy
from random import choice
#, get_surrounding_cells

def backtracking(inBoard: board):
    pass

def fwd_checking(inBoard: board) -> bool:

    noOptions = True
    for domain in inBoard.domains:
        if len(domain) > 1:
            noOptions = False
    
    if noOptions: return False

    minValues = get_MRV(inBoard)

    maxHeuristicFound = -1
    maxHeurisitcIdx = -1
    for cell in minValues:
        heuristic = get_degree_heuristic(cell, inBoard)
        if heuristic > maxHeuristicFound:
            maxHeuristicFound = heuristic
            maxHeurisitcIdx = cell
    

    idxAsCoord = idx_to_coord(maxHeurisitcIdx)
    boardToCheck = deepcopy(inBoard)
    valuesToCheck = boardToCheck.domains[maxHeurisitcIdx]
    newValue = valuesToCheck.pop(0)

    while len(valuesToCheck) > 0:
        if (boardToCheck.can_be_placed(idxAsCoord[0], idxAsCoord[1], newValue)):
            boardToCheck.set_value_at(idxAsCoord[0], idxAsCoord[1], newValue)
            if not fwd_checking(boardToCheck):
                newValue = valuesToCheck.pop(0)
            else:
                inBoard.set_value_at(idxAsCoord[0], idxAsCoord[1], newValue)
                return True
        else:
            newValue = valuesToCheck.pop(0)
    
    return False

#returns an array of indices
def get_MRV(inBoard: board): 
    minLen: int = 9
    idx_list = []
    for domain in inBoard.domains:
        if len(domain) < minLen:
            minLen = len(domain)
    for idx in range(0, len(inBoard.domains)):
        domain = inBoard.domains[idx]
        if len(domain)==minLen:
            idx_list.append(idx)
    return idx_list


#TODO: get a better understanding of what a degree heuristic is
#for now we'll just go with that

# returns degree heuristic at a given position (the position must be defined as a tuple)
def get_degree_heuristic(position, inBoard: board) -> int:
    degree = 0
    for point in inBoard.get_surrounding_cells(position):
        if len(inBoard.domains[point]) > 1:
            degree += 1
    return degree

def solve_sudoku(inBoard: board):
    print(fwd_checking(inBoard))
