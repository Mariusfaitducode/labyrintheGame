import random

from constante import *
from affichage import *


def init_lab():

    grid = [[0 for _ in range(NB_COLUMN)] for _ in range(NB_LINE)]

    count = 0

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            if l % 2 == 0:
                grid[l][c] = WALL

            else:
                if c % 2 == 0:
                    grid[l][c] = WALL
                else:
                    grid[l][c] = count
                    count += 1
    return grid


def re_init_lab(grid, cnv):

    count = 0

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            if l % 2 == 0:
                grid[l][c] = WALL

            else:
                if c % 2 == 0:
                    grid[l][c] = WALL
                else:
                    grid[l][c] = count
                    count += 1

    draw_grid(cnv, grid)


def generate_lab(grid, cnv):

    wall_list = init_wall_list(grid)

    count_list = init_count_list(grid)

    #for i in range(50):
    while not check_finish(grid):

        rand = random.randint(0, len(wall_list) - 1)
        l, c = wall_list[rand]

        if grid[l][c + 1] != grid[l][c - 1]:

            if grid[l][c + 1] != WALL and grid[l][c-1] != WALL:

                grid[l][c] = grid[l][c + 1] = grid[l][c - 1] = compare_val(count_list, grid[l][c + 1], grid[l][c - 1])

                for i in range(-1, 2):
                    draw_case(cnv, grid, l, c+i)

                wall_list.remove((l, c))

                same_color(grid, l, c + 1, grid[l][c], cnv)
                same_color(grid, l, c - 1, grid[l][c], cnv)

        elif grid[l + 1][c] != grid[l - 1][c]:

            if grid[l + 1][c] != WALL and grid[l - 1][c] != WALL:

                grid[l][c] = grid[l + 1][c] = grid[l - 1][c] = compare_val(count_list, grid[l + 1][c], grid[l - 1][c])

                for i in range(-1, 2):
                    draw_case(cnv, grid, l+i, c)

                wall_list.remove((l, c))

                same_color(grid, l + 1, c, grid[l][c], cnv)
                same_color(grid, l - 1, c, grid[l][c], cnv)

    final_value = grid[1][1]

    grid[DEPART[0]][DEPART[1]] = final_value
    draw_case(cnv, grid, DEPART[0], DEPART[1])

    grid[ARRIVE[0]][ARRIVE[1]] = final_value
    draw_case(cnv, grid, ARRIVE[0], ARRIVE[1])

    cnv.update()

    # print(str(final_value) + "-->" + str(count_list[final_value]))


def compare_val(count_list, val1, val2):

    if count_list[val1] > count_list[val2]:
        count_list[val1] += 1
        count_list[val2] = 0
        return val1
    else:
        count_list[val2] += 1
        count_list[val1] = 0
        return val2


def check_finish(grid):

    val = grid[1][1]

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            if grid[l][c] != WALL:

                if val != grid[l][c]:
                    return False

    return True


def same_color(grid, l, c, val, cnv):

    for i in range (-1, 2):
        # print(i)

        if i != 0:
            if grid[l+i][c] != WALL:
                if grid[l+i][c] != val:

                    grid[l + i][c] = grid[l][c]
                    draw_case(cnv, grid, l + i, c)

                    same_color(grid, l + i, c, val, cnv)

            if grid[l][c+i] != WALL:
                if grid[l][c + i] != val:

                    grid[l][c + i] = grid[l][c]
                    draw_case(cnv, grid, l, c + i)

                    same_color(grid, l, c + i, val, cnv)


def init_wall_list(grid):

    list = []

    for l in range(1, NB_LINE - 1):
        for c in range(1, NB_COLUMN - 1):

            if grid[l][c] == WALL:
                list.append((l, c))

    return list


def init_count_list(grid):

    list = []

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            if grid[l][c] != WALL:
                list.append(1)

    return list

