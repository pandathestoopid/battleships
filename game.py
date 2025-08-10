from tkinter import *

import grid
import drydock
import ai


class Game:
    def __init__(self, root, colors):
        self.root = root
        self.colors = colors
        self.color = colors[0]
        self.textColor = colors[1]
        self.accentColor1 = colors[2]
        self.accentColor2 = colors[3]

        # Boards for the player and AI, stored in 2D lists
        self.plyBoard = []
        self.aiBoard = []


    def on_ships_placed(self, currentBoard):
        print('control handed back to game file.')
        currentBoard = grid.board

    # Starts the game by generating the grid and sidebar
    def start(self):

        gridPly = grid.Grid(10, root=self.root, colors=self.colors, user='You')
        gridAi = grid.Grid(10, root=self.root, colors=self.colors, user='AI')

        gridTitle = Label(self.root, text='\u2192  Place your Ships', font=('Inter', 45, 'bold'), padx=25, pady=5, fg='green',
                          bg=self.color, anchor='w')
        gridTitle.grid(column=0, row=0, sticky='w')


        gridPly.generate(2)
        gridPly.start_ship_placement(doneCallback=lambda: self.on_ships_placed(self.plyBoard))
        gridAi.generate(1)
        gridAi.start_ship_placement(doneCallback=lambda: self.on_ships_placed(self.aiBoard))