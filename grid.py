from tkinter import *

import warships

squares = []

# Test, value should be false
shipsPlaced = False


class Grid:
    def __init__(self, size, root, colors, user):
        self.gridSize = size
        self.root = root
        self.color = colors[0]
        self.textColor = colors[1]
        self.accentColor1 = colors[2]
        self.accentColor2 = colors[3]
        self.user = user

        # 2D list of buttons for later reference
        self.buttons = [[None for _ in range(size)] for _ in range(size)]

        # Another 2D list that stores the game state
        self.board = [[None for _ in range(size)] for _ in range(size)]

        # Ship preview options
        self.shipOrientation = 'horizontal' # Can be changed to vertical

        # Which ship is being previewed/placed
        self.shipIndex = 0


    # Generates the grid with its buttons
    def generate(self, pos):

        # Makes a frame for the game
        self.playerFrame = Frame(self.root, bg=self.color)
        self.playerFrame.grid(column=0, row=pos, padx=10, pady=15, sticky='n')

        titleLabel = Label(self.playerFrame, text=f'{self.user}', font=('Inter', 20, 'bold'), bg=self.color, fg=self.textColor, width=5, anchor='e')
        titleLabel.grid(column=0, row=0, padx=10, pady=5, sticky='nw')

        # Makes a frame for the grid
        gridFrame = Frame(self.playerFrame, bg=self.color)
        gridFrame.grid(column=1, row=0, padx=5, pady=5)

        # Adds the buttons to the grid
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        for row in range(self.gridSize):
            for col in range(self.gridSize):
                square = Button(
                    gridFrame, bg=self.accentColor1, activebackground=self.accentColor2, width=3, height=1, relief='ridge',
                    command=lambda r=letters[row], c=col+1: self.click(r, c))
                square.grid(column=col+1, row=row+1)

                # Store buttons in 1 and 2D list
                self.buttons[row][col] = square
                squares.append(square)


        # Labels for the top row (numbers)

        for num in range(self.gridSize):
            numLabel = Label(gridFrame, text=num+1, bg=self.color, fg=self.textColor, font=('Courier New', 10))
            numLabel.grid(column=num+1, row=0)

        # Labels for the left column (letters)

        for letter in letters:
            letterLabel = Label(gridFrame, text=letter, bg=self.color, fg=self.textColor, padx=8, font=('Courier New', 10))
            letterLabel.grid(column=0, row=letters.index(letter)+1)

    # Highlights multiple squares for ship placing
    def highlight_ship(self, row, col, highlight, size):
        for i in range(size):
            try:
                if self.shipOrientation == 'horizontal':
                    if self.board[row][col + i] is not None:
                        break
                    self.buttons[row][col + i].config(bg=highlight)
                elif self.shipOrientation == 'vertical':
                    if self.board[row + i][col] is not None:
                        break
                    self.buttons[row + i][col].config(bg=highlight)
            except IndexError:
                break  # Stops if out of bounds

    # When the mouse hovers over a button
    def on_button_enter(self, event, row, col, size):
        self.highlight_ship(row, col, '#999', size)

    # When the mouse is not hovering over a button, size+1 is to remove the extra square no longer covered when the selection gets smaller
    def on_button_leave(self, event, row, col, size):
        self.highlight_ship(row, col, self.accentColor1, size + 1)

    # Begins the ship placement process
    def start_ship_placement(self):

        if self.shipIndex >= len(warships.ships):
            print('All ships placed, may the best Admiral win!')
            # Will make this start the game, return is temporary
            return

        # Sets the attributes for the current ship that is being placed
        currentShip = warships.ships[self.shipIndex]
        self.shipType = currentShip['name']
        self.shipSize = currentShip['size']

        self.shipLabel = Label(self.playerFrame, text=f'{self.shipType.upper()}  [{self.shipSize}]', font=('Inter', 15, 'bold'), padx=50, pady=15, bg=self.color, fg='pale green', anchor='w')
        self.shipLabel.grid(column=2, row=0, sticky='nw')

        for row in range(self.gridSize):
            for col in range(self.gridSize):

                square = self.buttons[row][col]

                # Bind the hovering methods and passes the size to the highlighing method
                square.bind("<Enter>", lambda event, r=row, c=col: self.on_button_enter(event, r, c, self.shipSize))
                square.bind("<Leave>", lambda event, r=row, c=col: self.on_button_leave(event, r, c, self.shipSize))

    # Locks a square the user clicked on
    def click(self, x, y):
        if not shipsPlaced:
            self.place(x, y)
        else:
            self.lock(x, y)
        return





    # Places the ship after clicking the desired square and resets to run ship placement again
    def place(self, x, y):
        print(x,y)

        self.shipIndex += 1
        self.shipLabel.destroy()
        self.start_ship_placement()

    # Locks the square after clicking the desired square
    def lock(self, x, y):
        pass

