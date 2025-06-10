from tkinter import *
from grid import *

import shop


# Window specs

root = Tk()
root.geometry('900x600')
root.title('Battleships')
root.configure(bg='white', border=25)
root.resizable(False, False)


# Grid routine, will put into something else soon

userGrid = Grid(10, root = root)
userGrid.generate(0)
userGrid.start_ship_placement()

root.mainloop()