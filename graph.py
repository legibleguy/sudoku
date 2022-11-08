def coord_to_idx(coordX: int, coordY: int, boardSizeX = 9, boardSizeY = 9):
    coord = (coordY * boardSizeX) + coordX
    if coord >= boardSizeX * boardSizeY: return -1
    else: return coord 

def idx_to_coord(idx: int, boardSizeX = 9, boardSizeY = 9):
    return [int(idx / boardSizeX), idx % boardSizeX]

class board:
    def __init__(self) -> None:
        self.values = [0] * 81
        self.domains = []
        self.__zones = [[0, 1, 2, 9, 10, 11, 18, 19, 20], [3, 4, 5, 12, 13, 14, 21, 22, 23], [6, 7, 8, 15, 16, 17, 24, 25, 26],
                    [27, 28, 29, 36, 37, 38, 45, 46, 47], [30, 31, 32, 39, 40, 41, 48, 49, 50], [33, 34, 35, 42, 43, 44, 51, 52, 53],
                    [54, 55, 56, 63, 64, 65, 72, 73, 74], [57, 58, 59, 66, 67, 68, 75, 76, 77], [60, 61, 62, 69, 70, 71, 78, 79, 80]]
        
        for i in range(0, 81): self.domains.append([1,2,3,4,5,6,7,8,9])

    def __get_zone_at_point(self, atX: int, atY : int):
        idx = coord_to_idx(atX, atY)
        for zone in self.__zones:
            if idx in zone: return zone.copy()
        return []

    def __get_neighbors(self, atX : int, atY : int):
        idx = coord_to_idx(atX, atY)
        outNeighbors = self.__get_zone_at_point(atX, atY)
        outNeighbors.remove(idx)

        for x in range(0, atX):
            neighb_idx = coord_to_idx(x, atY)
            if neighb_idx not in outNeighbors: outNeighbors.append(neighb_idx)
            else: break
        for x in range(atX+1, 9):
            neighb_idx = coord_to_idx(x, atY)
            if neighb_idx not in outNeighbors: outNeighbors.append(neighb_idx)
        for y in range(0, atY):
            neighb_idx = coord_to_idx(atX, y)
            if neighb_idx not in outNeighbors: outNeighbors.append(neighb_idx)
            else: break
        for y in range(atY+1, 9):
            neighb_idx = coord_to_idx(atX, y)
            if neighb_idx not in outNeighbors: outNeighbors.append(neighb_idx)
        
        return outNeighbors
    
    def can_be_placed(self, atX : int, atY : int, value : int) -> bool:
        idx = coord_to_idx(atX, atY)
        
        for neighb in self.__get_neighbors(atX, atY):
            if self.values[neighb] == value: return False
        
        return True
    
    def set_value_at(self, atX : int, atY : int, value : int) -> bool:

        idx = coord_to_idx(atX, atY)
        self.values[idx] = value
        self.domains[idx] = [value]

        for neighb in self.__get_neighbors(atX, atY):
            if value in self.domains[neighb]: 
                self.domains[neighb].remove(value)