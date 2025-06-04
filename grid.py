from tkinter import *
from functools import partial

from ships import *

root = Tk()
root.geometry('900x600')
root.title('Battleships')
root.configure(bg='white', border=25)
root.resizable(False, False)

squares = []

# Test, value should be false
shipsPlaced = False


class Grid:
    def __init__(self, size):
        self.size = size

        # 2D list of buttons for later reference
        self.buttons = [[None for _ in range(size)] for _ in range(size)]

        # Ship preview options
        self.shipSize = 3  # This is a placeholder

    # Locks a square the user clicked on
    def click(self, x, y):
        if not shipsPlaced:
            userGrid.placeShip(x, y)
        else:
            userGrid.lock(x, y)
        return

    # When the mouse hovers over a button
    def on_button_enter(self, event):
        event.widget.config(bg="gray")

    # When the mouse is not hovering over a button
    def on_button_leave(self, event):
        event.widget.config(bg="#eee")

    # Generates the grid with its buttons
    def generate(self, framePos):

        # Makes a frame for the grid
        gridFrame = Frame(root, bg='white')
        gridFrame.grid(column=framePos, row=0, padx=10, pady=10)

        # Adds the buttons to the grid
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        for row in range(self.size):
            for col in range(self.size):
                square = Button(
                    gridFrame, bg='#eee', activebackground='#ddd', width=3, height=1, relief='ridge', command=lambda y=row+1, x=letter[col]: self.click(x, y))

                square.grid(column=col, row=row)

                # Bind the hovering methods
                square.bind("<Enter>", self.on_button_enter)
                square.bind("<Leave>", self.on_button_leave)

                # Store buttons in 1 and 2D list
                self.buttons[row][col] = square
                squares.append(square)

        print(squares)

    def placeShip(self, x, y):
        pass

    def lock(self, x, y):
        pass




gridSize = 10

userGrid = Grid(gridSize)
userGrid.generate(0)
root.mainloop()