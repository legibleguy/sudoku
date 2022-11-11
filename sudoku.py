from graph import board, idx_to_coord
#, get_surrounding_cells

def backtracking(inBoard: board):
    pass

def fwd_checking(inBoard: board):
    pass

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

# returns degree heuristic at a given position (the position must be defined as a tuple)
def get_degree_heuristic(position, inBoard: board) -> int:
    pass

def solve_sudoku(inBoard: board):
    pass
