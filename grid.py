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
shipsPlaced = True


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

        # Makes a frame for the game
        playerFrame = Frame(root, bg='white')
        playerFrame.grid(column=framePos, row=0, padx=10, pady=10)

        # Makes a frame for the grid
        gridFrame = Frame(playerFrame, bg='white')
        gridFrame.grid(column=1, row=1, padx=5, pady=5)

        # Adds the buttons to the grid
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        for row in range(self.size):
            for col in range(self.size):
                square = Button(
                    gridFrame, bg='#eee', activebackground='#ddd', width=3, height=1, relief='ridge', command=lambda r=letters[row], c=col+1: self.click(r, c))

                square.grid(column=col+1, row=row+1)

                # Bind the hovering methods
                square.bind("<Enter>", self.on_button_enter)
                square.bind("<Leave>", self.on_button_leave)

                # Store buttons in 1 and 2D list
                self.buttons[row][col] = square
                squares.append(square)


        # Labels for top row (numbers)

        for num in range(self.size):
            numLabel = Label(gridFrame, text=num+1, bg='white', font=('Courier New', 10))
            numLabel.grid(column=num+1, row=0)

        # Labels for left column (letters)

        for letter in letters:
            letterLabel = Label(gridFrame, text=letter, bg='white', padx=8, font=('Courier New', 10))
            letterLabel.grid(column=0, row=letters.index(letter)+1)


    def placeShip(self, x, y):
        pass

    def lock(self, x, y):
        carrier.attack(x, y)




gridSize = 10

userGrid = Grid(gridSize)
userGrid.generate(0)
root.mainloop()