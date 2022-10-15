from generation import *
from resolution import *
from generation2 import *
from tkinter import *

window = Tk()
window.title("Test fenetre")
window.geometry("1580x920")

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

but3.place(x=2 * TAB_GAP + WIDTH_TAB, y=3 * TAB_GAP + 3 * COTE_CASE)

grid = generate_lab_2(grid, cnv)

draw_grid(cnv, grid)

# resolve_lab(grid)

# parcours_A_star(grid)



window.mainloop()
