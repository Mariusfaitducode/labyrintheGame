# import time
import time

from constante import *

import hashlib


def draw_grid(cnv, grid):

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            x1 = c * COTE_CASE
            y1 = l * COTE_CASE
            x2 = x1 + COTE_CASE
            y2 = y1 + COTE_CASE

            if grid[l][c] == -1:
                cnv.create_rectangle(x1, y1, x2, y2, fill='black', width=0)
            else:
                color = id_to_random_color(grid[l][c])
                #str(color)
                cnv.create_rectangle(x1, y1, x2, y2, fill='#'+color, width=0)


def draw_final_grid(cnv, grid):

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            x1 = c * COTE_CASE
            y1 = l * COTE_CASE
            x2 = x1 + COTE_CASE
            y2 = y1 + COTE_CASE

            if grid[l][c] == -1:
                cnv.create_rectangle(x1, y1, x2, y2, fill='black', width=0)
            else:
                cnv.create_rectangle(x1, y1, x2, y2, fill='white', width=0)



def draw_case(cnv, grid, l, c):

    x1 = c * COTE_CASE
    y1 = l * COTE_CASE
    x2 = x1 + COTE_CASE
    y2 = y1 + COTE_CASE

    color = id_to_random_color(grid[l][c])
    cnv.create_rectangle(x1, y1, x2, y2, fill='#' + color, width=0)
    cnv.update()
    # time.sleep(0.01)


def draw_visited_case(cnv, l, c):

    x1 = c * COTE_CASE
    y1 = l * COTE_CASE
    x2 = x1 + COTE_CASE
    y2 = y1 + COTE_CASE

    cnv.create_rectangle(x1, y1, x2, y2, fill='yellow', width=0)
    cnv.update()
    # time.sleep(0.0001)


def draw_colour_case(cnv, l, c, couleur):

    x1 = c * COTE_CASE
    y1 = l * COTE_CASE
    x2 = x1 + COTE_CASE
    y2 = y1 + COTE_CASE

    cnv.create_rectangle(x1, y1, x2, y2, fill=couleur, width=0)
    cnv.update()


def id_to_random_color(number):

    random_bytes = hashlib.sha1(bytes(number)).digest()
    color = [int(random_bytes[-1]), int(random_bytes[-2]), int(random_bytes[-3])]

    for i in range(3):
        if color[i] < 16:
            color[i] += (16 - color[i])
        if color[i] > 255:
            color[i] -= (color[i] - 255)

    result = f'{color[0]:x}' + f'{color[1]:x}' + f'{color[2]:x}'
    #print(color)
    #print(result)
    return result




