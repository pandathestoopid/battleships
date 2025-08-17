from tkinter import *

import warships

class Sidebar:
    def __init__(self, root, colors, ships):
        self.root = root
        self.colors = colors
        self.color = colors[0]
        self.textColor = colors[1]
        self.accentColor1 = colors[2]
        self.accentColor2 = colors[3]

        self.ships = ships
