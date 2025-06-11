from tkinter import *
from tkinter import font
import os

import grid
import shop


# Window specs

root = Tk()
root.geometry('1600x900')
root.title('Battleships')
root.configure(bg='white', border=25)
root.resizable(False, False)

# Font specs

fontPath = os.path.join(os.getcwd(), 'Inter.ttf')
font.Font(root=root, name='Inter', size=11)

defaultFont = font.nametofont('TkDefaultFont')
defaultFont.configure(family='Inter', size=11)


# Grid routine, will put into something else soon

# userGrid = grid.Grid(10, root = root)
# userGrid.generate()
# userGrid.start_ship_placement()

shop = shop.Shop(root = root, country = 'United States')
shop.open()

root.mainloop()