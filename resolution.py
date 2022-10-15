# from constante import *
import math

from affichage import *


VISITED = 1
TO_VISIT = 0


def parcours_A_star(grid, cnv):

    possibility_list = []

    explo_grid = create_explo_grid(grid)
    count_grid = explo_grid

    (l, c) = DEPART
    count = 2

    explo_grid[l][c] = VISITED
    draw_visited_case(cnv, l, c)
    count_grid[l][c] = count

    l += 1
    count += 1

    explo_grid[l][c] = VISITED
    draw_visited_case(cnv, l, c)
    count_grid[l][c] = count

    count += 1

    # (l, c) = actual_case

    while (l, c) != ARRIVE:

        for i in range(-1, 2, 2):

            if explo_grid[l + i][c] == TO_VISIT:

                poids = count + norme_vect((l + i, c), ARRIVE)

                possibility_list.append(((l + i, c), poids, count))

            if explo_grid[l][c + i] == TO_VISIT:

                poids = count + norme_vect((l, c + i), ARRIVE)

                possibility_list.append(((l, c + i), poids, count))

        (l, c), count_case = choose_case(possibility_list, cnv)

        explo_grid[l][c] = VISITED
        draw_visited_case(cnv, l, c)

        count_grid[l][c] = count_case

        count = count_case + 1
        # print(count)

    print("finishhh")

    for row in count_grid:
        print('| '.join([str(elem) for elem in row]))

    draw_passing_case(cnv, l, c, 'red')
    print(count_grid[l][c])
    count -= 1

    while (l, c) != DEPART and count > -100:

        # print("ok")
        count -= 1
        print(count)

        for i in range(-1, 2, 2):

            if count_grid[l + i][c] != WALL:
                if count_grid[l + i][c] == count:
                    l = l + i

                    print(count_grid[l][c])
                    draw_passing_case(cnv, l, c, 'red')
                    break

            if count_grid[l][c + i] != WALL:
                if count_grid[l][c + i] == count:

                    c = c + i

                    print(count_grid[l][c])
                    draw_passing_case(cnv, l, c, 'red')
                    break
    print("end of path")


def choose_case(possibility_list, cnv):

    min = 1000000
    final_ref = (0, 0)
    final_count = 0

    for i in range(len(possibility_list)):

        ref, poids, count = possibility_list[i]

        # draw_passing_case(cnv, ref[0], ref[1], 'red')

        if poids < min:

            min = poids
            final_ref = ref
            final_count = count

    possibility_list.remove((final_ref, min, final_count))
    return final_ref, final_count


def norme_vect(u, v):

    (x1, y1) = u
    (x2, y2) = v

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def create_explo_grid(grid):

    explo_grid = [[0 for _ in range(NB_COLUMN)] for _ in range(NB_LINE)]

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            if grid[l][c] == WALL:

                explo_grid[l][c] = WALL

            else:
                explo_grid[l][c] = TO_VISIT

    return explo_grid


def first_step(explo_grid, first_case):

    (l, c) = first_case

    for i in range(-1, 2, 2):

        if 0 < l + i < NB_LINE - 1:

            if explo_grid[l + i][c] == TO_VISIT:

                l = l + i
                break

        if 0 < c + i < NB_COLUMN - 1:
            if explo_grid[l][c + i] == TO_VISIT:

                c = c + i
                break

    return l, c



def first_step_way_back(count_grid,last_case, count):

    (l, c) = last_case

    for i in range(-1, 2, 2):

        if 0 < l + i < NB_LINE - 1:

            if count_grid[l + i][c] == count:

                l = l + i
                break

        if 0 < c + i < NB_COLUMN - 1:
            if count_grid[l][c + i] == count:

                c = c + i
                break

    return l, c
