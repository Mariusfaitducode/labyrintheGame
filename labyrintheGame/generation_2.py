import random

from affichage import *
from resolution import *


def generate_by_explo(grid, cnv):

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            if grid[l][c] != WALL:

                grid[l][c] = TO_VISIT

    # draw_grid(cnv, grid)

    l = 0
    c = 0

    while grid[l][c] == WALL:

        l = random.randint(0, NB_LINE-1)
        c = random.randint(0, NB_COLUMN-1)

    grid[l][c] = VISITED  # point de départ

    START = (l, c)

    break_the_walls(l, c, grid, START, cnv)

    draw_grid(cnv, grid)

    grid[DEPART[0]][DEPART[1]] = VISITED
    draw_case(cnv, grid, DEPART[0], DEPART[1])

    grid[ARRIVE[0]][ARRIVE[1]] = VISITED
    draw_case(cnv, grid, ARRIVE[0], ARRIVE[1])

    # return grid


def break_the_walls(l, c, grid, START, cnv):

    possibility_list = wall_list(grid, l, c)

    result = len(possibility_list)

    if result == 0 and (l, c) == START:
        print("finish")
        return True

    elif result > 0:

        rand = random.randint(0, len(possibility_list) - 1)

        l2, c2 = possibility_list[rand]

        grid[l2][c2] = VISITED

        draw_visited_case(cnv, l2, c2)

        l3 = 2 * l2 - l
        c3 = 2 * c2 - c

        grid[l3][c3] = VISITED

        draw_visited_case(cnv, l3, c3)

        if not break_the_walls(l3, c3, grid, START, cnv):
            break_the_walls(l, c, grid, START, cnv)

    else:
        return False


def wall_list(grid, l, c):

    possible_list = []

    for i in range(-1, 2, 2):

        if grid[l + i][c] == WALL:
            if 0 < l + 2 * i < NB_LINE and grid[l + 2 * i][c] == TO_VISIT:

                possible_list.append((l + i, c))

        if grid[l][c + i] == WALL:
            if 0 < c + 2 * i < NB_COLUMN and grid[l][c + 2 * i] == TO_VISIT:

                possible_list.append((l, c + i))

    return possible_list
