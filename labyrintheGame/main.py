import affichage
from generation import *
from generation_2 import *
from resolution import *
from tkinter import *

import save

window = Tk()
window.title("Test fenetre")
window.geometry("1280x720")

cnv = Canvas(window, width=WIDTH_TAB, height=HEIGHT_TAB, background='light gray')
cnv.pack()
cnv.place(x=TAB_GAP, y=TAB_GAP)

grid = init_lab()

but1 = Button(window, text="Générer", font='Helvetica 15 bold',
              background='light gray', command=(lambda: generate_lab(grid, cnv)))

but1.place(x=2 * TAB_GAP + WIDTH_TAB, y=TAB_GAP + 3 * COTE_CASE)

but2 = Button(window, text="Réinitialiser", font='Helvetica 15 bold',
              background='light gray', command=(lambda: re_init_lab(grid, cnv)))

but2.place(x=2 * TAB_GAP + WIDTH_TAB, y=2 * TAB_GAP + 3 * COTE_CASE)

but3 = Button(window, text="Résoudre", font='Helvetica 15 bold',
              background='light gray', command=(lambda: parcours_A_star(grid, cnv)))

but3.place(x=2 * TAB_GAP + WIDTH_TAB, y=4 * TAB_GAP + 3 * COTE_CASE)

but4 = Button(window, text="Génerer 2", font='Helvetica 15 bold',
              background='light gray', command=(lambda: generate_by_explo(grid, cnv)))

but4.place(x=2 * TAB_GAP + WIDTH_TAB, y=3 * TAB_GAP + 3 * COTE_CASE)

but5 = Button(window, text="Record", font='Helvetica 15 bold',
              background='light gray', command=(lambda: save.record_lab(grid)))

but5.place(x=2 * TAB_GAP + WIDTH_TAB, y=6 * TAB_GAP + 3 * COTE_CASE)

but6 = Button(window, text="Clear", font='Helvetica 15 bold',
              background='light gray', command=(lambda: affichage.draw_final_grid(cnv, grid)))

but6.place(x=2 * TAB_GAP + WIDTH_TAB, y=8 * TAB_GAP + 3 * COTE_CASE)


# grid = generate_by_explo(grid, cnv)

# draw_grid(cnv, grid)

# resolve_lab(grid)

# parcours_A_star(grid)


window.mainloop()
