def coord_to_idx(coordX: int, coordY: int, boardSizeX = 9, boardSizeY = 9):
    return (coordY * boardSizeX) + coordX

def idx_to_coord(idx: int, boardSizeX = 9, boardSizeY = 9):
    return [int(idx / boardSizeX), idx % boardSizeX]

class board:
    def __init__(self) -> None:
        self.values = [0] * 81
        self.domains = [[1,2,3,4,5,6,7,8,9]] * 81
    
    def set_value_at(self, atX : int, atY : int, value : int):
        idx = coord_to_idx(atX, atY)
        self.values[idx] = value
        self.domains[idx] = [value]
