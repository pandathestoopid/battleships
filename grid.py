from tkinter import *

import warships
import ai

# Initialized global variables
board = []

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

        # Defines the letters used on the grid
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        # If all ships are placed
        self.shipsPlaced = False

        # Defines if AI is running ship placing
        self.auto = False

        # Initializes the AI placing program
        self.placer = ai.Placer(3, 10)

        # Determines whether ships are intitially visible based on whose grid this is, temporarily commented for testing
        self.visible = True # if user == 'You' else False


    # Generates the grid with its buttons
    def generate(self, pos):

        # Makes a frame for the game
        self.playerFrame = Frame(self.root, bg=self.color)
        self.playerFrame.grid(column=0, row=pos, padx=10, pady=15, sticky='nw')

        titleLabel = Label(self.playerFrame, text=f'{self.user}', font=('Inter', 20, 'bold'), bg=self.color, fg=self.textColor, width=5, anchor='e')
        titleLabel.grid(column=0, row=0, padx=10, pady=5, sticky='nw')

        # Makes a frame for the grid
        gridFrame = Frame(self.playerFrame, bg=self.color)
        gridFrame.grid(column=1, row=0, padx=5, pady=5)

        # Adds the buttons to the grid
        for row in range(self.gridSize):
            for col in range(self.gridSize):
                square = Button(
                    gridFrame, state='disabled', bg=self.accentColor1, activebackground=self.accentColor2, width=3, height=1, relief='ridge',
                    command=lambda r=row, c=col: self.click(r, c)) # Sends raw data
                square.grid(column=col+1, row=row+1)

                # Store buttons in 2D list
                self.buttons[row][col] = square


        # Labels for the top row (numbers)

        for num in range(self.gridSize):
            numLabel = Label(gridFrame, text=num+1, bg=self.color, fg=self.textColor, font=('Courier New', 10))
            numLabel.grid(column=num+1, row=0)

        # Labels for the left column (letters)

        for letter in self.letters:
            letterLabel = Label(gridFrame, text=letter, bg=self.color, fg=self.textColor, padx=8, font=('Courier New', 10))
            letterLabel.grid(column=0, row=self.letters.index(letter)+1)


    # Rotates the ship placer
    def rotate_ship(self):
        if self.shipOrientation == 'horizontal':
            self.shipOrientation = 'vertical'
        elif self.shipOrientation == 'vertical':
            self.shipOrientation = 'horizontal'

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

    # Automatically places the ships
    def autoPlace(self):
        for sType in warships.ships: # Goes through the 5 types of ships in the main ship library
            self.shipSize = sType['size'] # Pulls the type's size from its dictionary
            self.shipType = sType['name'] # Pulls the type's name from its dictionary
            x, y, self.shipOrientation = self.placer.place(self.shipSize)
            self.place(y,x)

    # Begins the ship placement process
    def start_ship_placement(self, doneCallback=None):

        # Checks if this is the AI board, if so, enables auto-placing; if not, enables the buttons to manually place
        if self.user == 'AI':
            self.auto = True
            self.autoPlace()
        else:
            for row in self.buttons:
                for button in row:
                    button.config(state='normal')

        # Sets up callback function and only writes when one is passed from the parent file
        if doneCallback is not None:
            self.doneCallback = doneCallback

        # Rotate button, which appears only if the grid user is the player
        if self.user == 'You':
            rotateButton = Button(self.playerFrame, text='Rotate \u21BA', font=('Inter', 12, 'bold'), bg='#006abb',
                                  fg='#fff', relief='flat', padx=15, command=self.rotate_ship)
            rotateButton.grid(column=1, row=1, pady=15)

        # Routine before passing back to game.py
        if self.shipIndex >= len(warships.ships):
            print('All ships placed, may the best Admiral win!')
            self.shipSize = 0 # Removes highlight
            global board
            board = self.board
            self.shipsPlaced = True
            rotateButton.destroy()
            self.doneCallback() # Callback function
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
    def click(self, y, x):
        if not self.shipsPlaced:
            self.place(y, x)
        else:
            self.lock(y, x)
        return

    # Places the ship after clicking the desired square
    def place(self, y, x):

        while True:
            try:
                if self.shipOrientation == 'horizontal':
                    # Checks that the ship will fit
                    if x + self.shipSize > self.gridSize:
                        raise IndexError

                    # Checks if the ship collides with another
                    for s in range(self.shipSize):
                        if self.board[y][x+s] is not None:
                            raise IndexError

                    # Places the ship and updates the buttons one square at a time
                    for s in range(self.shipSize):
                        self.board[y][x+s] = self.shipType
                        if self.visible:
                            self.buttons[y][x+s].config(bg='#AAA', relief='sunken')

                elif self.shipOrientation == 'vertical':
                    # Checks that the ship will fit
                    if y + self.shipSize > self.gridSize:
                        raise IndexError

                    # Checks if the ship collides with another
                    for s in range(self.shipSize):
                        if self.board[y+s][x] is not None:
                            raise IndexError

                    # Places the ship and updates the buttons one square at a time
                    for s in range(self.shipSize):
                        self.board[y+s][x] = self.shipType
                        if self.visible:
                            self.buttons[y+s][x].config(bg='#AAA', relief='sunken')
                # Once placement is successful, the while loop ends
                break
            except IndexError:
                oobLabel = Label(self.playerFrame, text='ERROR: Out of bounds', font=('Inter', 20, 'bold'), padx=40, pady=15, bg='red', fg='#fff')
                oobLabel.grid(column=1, row=0, sticky='ew')
                oobLabel.after(1500, oobLabel.destroy)
                return


        # Moves to the next ship, resets the label, and repeats the process (only if ships are being placed manually)
        if not self.auto:
            self.shipIndex += 1
            self.shipLabel.destroy()
            self.start_ship_placement()

    # Locks the square after clicking the desired square
    def lock(self, y, x):
        pass

    # Get the board state

