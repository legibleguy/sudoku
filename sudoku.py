from graph import board, idx_to_coord
from copy import deepcopy
from random import choice
from graph_debug import draw_board, draw_board_domain_lenghts
#, get_surrounding_cells

def backtracking(inBoard: board):
    pass

def fwd_checking(inBoard: board) -> bool:

    noOptions = True
    for domain in inBoard.domains:
        if len(domain) > 1:
            noOptions = False
        if len(domain) == 0:
            print("can't decide what to put in one of the cells")
            return False
    if noOptions: 
        print("All cells have been set.")
        for idx in range(len(inBoard.values)):
            if inBoard.values[idx] == 0:
                inBoard.values[idx] = inBoard.domains[idx][0]

        return True

    minValues = get_MRV(inBoard)
    print("MRV is " + str(minValues))

    maxHeuristicFound = -1
    maxHeurisitcIdx = -1
    for cell in minValues:
        heuristic = get_degree_heuristic(cell, inBoard)
        if heuristic > maxHeuristicFound:
            maxHeuristicFound = heuristic
            maxHeurisitcIdx = cell
    print("Our of those MRVs, we chose cell #" + str(maxHeurisitcIdx))

    idxAsCoord = idx_to_coord(maxHeurisitcIdx)
    boardToCheck = deepcopy(inBoard)
    valuesToCheck = boardToCheck.domains[maxHeurisitcIdx].copy()
    newValue = valuesToCheck.pop(0)
    print("The first newValue value is " + str(newValue))

    while len(valuesToCheck) > 0:
        print("Right now we are checking " + str(newValue) + " at (" + str(idxAsCoord[0]) + ", " + str(idxAsCoord[1]) + ")")
        print(str(len(valuesToCheck)) + " values left to check")
        if (boardToCheck.can_be_placed(idxAsCoord[0], idxAsCoord[1], newValue)):
            boardToCheck.set_value_at(idxAsCoord[0], idxAsCoord[1], newValue)
            
            if boardToCheck.is_any_domain_zero(): 
                boardToCheck = deepcopy(inBoard)
                newValue = valuesToCheck.pop(0)
            else:
                draw_board(boardToCheck)
                draw_board_domain_lenghts(boardToCheck)
                if fwd_checking(boardToCheck):
                    # print("Setting a value")
                    inBoard.set_value_at(idxAsCoord[0], idxAsCoord[1], newValue)
                    return True
                else:
                    print("fwd_check has failed for value " + str(newValue) + " at " + str(idxAsCoord[0]) + ", " + str(idxAsCoord[1]))
                    print("Before popping the len of valuesToCheck is " + str(len(valuesToCheck)))
                    boardToCheck = deepcopy(inBoard)
                    newValue = valuesToCheck.pop(0)
                    print("After popping the len of valuesToCheck is " + str(len(valuesToCheck)))
        else:
            print("can_be_placed has failed for value " + str(newValue) + " at " + str(idxAsCoord[0]) + ", " + str(idxAsCoord[1]))
            newValue = valuesToCheck.pop(0)
    
    print("Ran out of options - returning false")
    return False

#returns an array of indices
def get_MRV(inBoard: board): 
    minLen: int = -1
    idx_list = []
    for domain in inBoard.domains:
        if minLen == -1 or len(domain) < minLen:
            if(len(domain) > 1): minLen = len(domain)

    for idx in range(len(inBoard.domains)):
        if(len(inBoard.domains[idx]) == 1): continue

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

def new_fwd_check(inBoard: board, checkAt, value) -> bool:
    boardToCheck = deepcopy(inBoard)
    #if not boardToCheck.can_be_placed(checkAt[0], checkAt[1], value): return False
    boardToCheck.set_value_at(checkAt[0], checkAt[1], value)

    for domain in boardToCheck.domains:
        if len(domain) == 0: return False
    
    return True

def solve_sudoku(inBoard: board):

    if len(inBoard.get_empty_cells()) == 0: return True

    minValues = get_MRV(inBoard)

    maxHeuristicFound = -1
    maxHeurisitcIdx = -1
    for cell in minValues:
        heuristic = get_degree_heuristic(cell, inBoard)
        if heuristic > maxHeuristicFound:
            maxHeuristicFound = heuristic
            maxHeurisitcIdx = cell

    idxAsCoord = idx_to_coord(maxHeurisitcIdx)
    valuesToCheck = inBoard.domains[maxHeurisitcIdx].copy()

    while len(valuesToCheck) > 0:
        toCheck = valuesToCheck.pop(0)
        boardBefore = deepcopy(inBoard)
        if new_fwd_check(inBoard, idxAsCoord, toCheck):
            inBoard.set_value_at(idxAsCoord[0], idxAsCoord[1], toCheck)
            if solve_sudoku(inBoard): return True
            else: inBoard = boardBefore
    
    return False


