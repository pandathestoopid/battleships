from tkinter import *
from functools import partial

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

    # Locks a square the user clicked on
    def click(self, x, y):
        if not shipsPlaced:
            userGrid.placeShip(x, y)
        else:
            userGrid.lock(x, y)
        return

    # Generates the grid with its buttons
    def generate(self, framePos):

        # Makes a frame for the grid
        gridFrame = Frame(root, bg='white')
        gridFrame.grid(column=framePos, row=0, padx=10, pady=10)

        # Adds the buttons to the grid
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        yNum = 0
        xNum = 0
        for row in range(self.size):
            for square in range(self.size):
                square = Button(
                    root, bg='#eee', activebackground='#ddd', width=3, height=1, relief='ridge', command=lambda y=yNum+1, x=letter[xNum]: self.click(x, y))
                square.grid(column=yNum, row=xNum)
                squares.append(square)
                yNum += 1
            yNum = 0
            xNum += 1
        print(squares)

    def placeShip(self, x, y):
        pass

    def lock(self, x, y):
        pass




gridSize = 10

userGrid = Grid(gridSize)
userGrid.generate(0)
root.mainloop()