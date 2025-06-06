from tkinter import *
from functools import partial

import warships

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
        self.shipOrientation = 'horizontal' # Can be changed to vertical

    # Locks a square the user clicked on
    def click(self, x, y):
        if not shipsPlaced:
            userGrid.place(x, y)
        else:
            userGrid.lock(x, y)
        return

    # Highlights multiple squares for ship placing
    def highlight_ship(self, row, col, highlight, size):
        for i in range(size):
            try:
                if self.shipOrientation == 'horizontal':
                    self.buttons[row][col+i].config(bg=highlight)
                elif self.shipOrientation == 'vertical':
                    self.buttons[row+i][col].config(bg=highlight)
            except IndexError:
                break # Stops if out of bounds

    # When the mouse hovers over a button
    def on_button_enter(self, event, row, col, size):
        self.highlight_ship(row, col, 'gray', size)

    # When the mouse is not hovering over a button
    def on_button_leave(self, event, row, col, size):
        self.highlight_ship(row, col, '#eee', size)

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

    # Begins ship placement process
    def start_ship_placement(self):

        # Imports ships from warships.py
        for ship in warships.ships:
            shipType = ship['name']
            size = ship['size']
            print(f'{shipType} is {size} squares long')

            for row in range(self.size):
                for col in range(self.size):

                    square = self.buttons[row][col]

                    # Bind the hovering methods
                    square.bind("<Enter>", partial(self.on_button_enter, row=row, col=col, size=size))
                    square.bind("<Leave>", partial(self.on_button_leave, row=row, col=col, size=size))

    def place(self, x, y):
        pass

    def lock(self, x, y):
        warships.carrier.attack(x, y)




gridSize = 10

userGrid = Grid(gridSize)
userGrid.generate(0)
userGrid.start_ship_placement()
root.mainloop()