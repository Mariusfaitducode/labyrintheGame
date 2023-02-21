from constante import *


def record_lab(grid):
    f = open("grid.txt", "w")

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):
            if grid[l][c] == WALL:
                f.write(str(1) + " ")
            else:
                f.write(str(0) + " ")

        f.write("\n")

    f.close()