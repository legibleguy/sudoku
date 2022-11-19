from graph import board

def draw_board(inBoard : board):
    toPrint: str = ""
    count = 0
    for y in range(0, 11):
        for x in range(0, 9):
            if y == 3 or y == 7:
                toPrint += " - "
                if x == 2 or x == 5:
                    toPrint += " | "
            else:
                toPrint += " " + str(inBoard.values[count]) + " "
                if x == 2 or x == 5:
                    toPrint += " | "
                count += 1
        toPrint += "\n"
    print(toPrint)
    
def draw_board_domain_lengths(inBoard : board):
    toPrint: str = ""
    count = 0
    for y in range(0, 11):
        for x in range(0, 9):
            if y == 3 or y == 7:
                toPrint += " - "
                if x == 2 or x == 5:
                    toPrint += " | "
            else:
                toPrint += " " + str(len(inBoard.domains[count])) + " "
                if x == 2 or x == 5:
                    toPrint += " | "
                count += 1
        toPrint += "\n"
    print(toPrint)
    
def draw_board_indices(inBoard : board):
    toPrint: str = ""
    count = 0
    for y in range(0, 11):
        for x in range(0, 9):
            if y == 3 or y == 7:
                toPrint += " - "
                if x == 2 or x == 5:
                    toPrint += " | "
            else:
                toPrint += " " + str(count) + " "
                if x == 2 or x == 5:
                    toPrint += " | "
                count += 1
        toPrint += "\n"
    print(toPrint)