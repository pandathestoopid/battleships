from functools import partial
from tkinter import *
from tkinter import font
import os
import time

import grid
import shop as shopFile
import warships


# Color theme

colorSetting = 'dark'

if colorSetting == 'light':
    color = '#fff'
    textColor = '#000'
    accentColor1 = '#eee'
    accentColor2 = '#ddd'
elif colorSetting == 'dark':
    color = '#111'
    textColor = '#fff'
    accentColor1 = '#222'
    accentColor2 = '#333'
else: # Else statement purely to avoid PyCharm warnings
    color = '#000'
    textColor = '#000'
    accentColor1 = '#000'
    accentColor2 = '#000'

colors = list((color, textColor, accentColor1, accentColor2))

# Window specs

root = Tk()
root.geometry('1600x900')
root.title('Battleships')
root.configure(bg=color, border=25)
root.resizable(False, False)

# Font specs

fontPath = os.path.join(os.getcwd(), 'Inter.ttf')
font.Font(root=root, name='Inter', size=10)

defaultFont = font.nametofont('TkDefaultFont')
defaultFont.configure(family='Inter', size=10)


# Load classes

shopObj = shopFile.Shop(root = root, country = warships.countries[0], colors=colors)


# Main menu window

class MainMenu:
    def open_menu(self):

        # Overall frame for the main menu
        self.menuFrame = Frame(root, bg=color, padx=100)
        self.menuFrame.grid(column=0, row=0)

        # Label for game title (will look better later)
        titleLabel = Label(self.menuFrame, text='Battleships', font=('Inter', 50, 'bold'), padx=50, pady=50,
                           fg='#006abb', bg=color)
        titleLabel.grid(column=0, row=0, sticky='nsew')

        # Play button
        self.playButton = Button(self.menuFrame, text='>>   Embark   <<', font=('Inter', 20, 'bold'), padx=5, pady=20,
                                 fg='white', bg='#006abb', relief='groove', command=self.opening_grid) # This passes the actual command to a later function so that the button is defined
        self.playButton.grid(column=0, row=1, sticky='nsew')

        # Frame for dock and shop button
        shipCustomizeFrame = Frame(self.menuFrame, bg=color, padx=0, pady=10)
        shipCustomizeFrame.grid(column=0, row=2, sticky='ew')

        # Dock button
        dockButton = Button(shipCustomizeFrame, text='Drydock', font=('Inter', 20), padx=62, pady=20, fg='white', bg='#006abb', relief='groove')
        dockButton.grid(column=0, row=0, sticky='ew')

        # Shop button
        self.shopButton = Button(shipCustomizeFrame, text='Shop', font=('Inter', 20), padx=78, pady=20, fg='white', bg='#006abb', relief='groove', command=self.open_shop)
        self.shopButton.grid(column=1, row=0, sticky='ew')

        # Exit button
        self.exitButton = Button(self.menuFrame, text='<<  Deboard  >>', font=('Inter', 20), padx=5, pady=20,
                                 fg='white', bg='#006abb', activebackground='#db4040', activeforeground='white', relief='groove', command=self.closing_game)
        self.exitButton.grid(column=0, row=3, sticky='ew')

        # Checker for aborting an animated button, flipped if abort button is pressed
        self.abort = False


    # Opens grid
    def opening_grid(self):
        self.button_animation(15, 0, 0, self.playButton, 'self.open_grid', 'Embarking', '>>', '<<', -1)

    # Opens shop
    def open_shop(self):

        # Opens the shop and checks for owned ships
        shopObj.open()
        shopObj.check_ships()

        # Sets the shop button to close it when pressed
        self.shopButton.config(relief='sunken', command=self.reopen_menu)

    # Reopens the main menu after closing the shop
    def reopen_menu(self):

        # Closes shop
        shopObj.shopFrame.destroy()

        # Resets shop button
        self.shopButton.config(relief='groove', command=self.open_shop)

    # Aborts game close if the close button is pressed during the animation
    def abort_game_close(self):
        self.abort = True
        self.exitButton.config(text='<<  Deboard  >>', font=('Inter', 20), padx=5, pady=20,
                               fg='white', bg='#006abb', activebackground='#db4040', activeforeground='white', relief='groove', command=self.closing_game)

    # Prepares to close the game
    def closing_game(self):

        self.abort = False # Sets checker to true again

        # Sets exit button to an abort button
        self.exitButton.config(text='<<  Abort  >>', bg='#db4040', activebackground='#db4040', activeforeground='white',
                               relief='sunken', command=self.abort_game_close)

        # Starts the closing button animation
        self.button_animation(0, 0, 18, self.exitButton, 'root.destroy', 'Abort', '<<', '>>', 1)

    # Animation for any button that has arrows
    def button_animation(self, passes, bigPasses, maxPasses, button, endCommand, btnText, animateeLeft, animateeRight, animationDirection):

        # Adds a space to the abort button string
        spaces = ' ' * passes

        # Checks if the end command should be executed or aborted
        if bigPasses == 5 and not self.abort: # Number of cycles before the end command is executed
            eval(f'{endCommand}()') # Evaluates the end command of the button animation
            return None
        elif self.abort: # Stops the function if the abort button is pressed
            return None

        # Updates the abort button string
        button.config(text=f'{animateeLeft}{spaces}  {btnText}  {spaces}{animateeRight}')

        # Updates the number of passes
        passes += animationDirection # Positive 1 moves the arrows away from the text, negative 1 moves them towards the text
        if passes == maxPasses: # Number of passes before the number of spaces are reset
            bigPasses += 1
            passes -= (maxPasses * animationDirection) # Resets passes to original value

        # Animation that re-runs the function with all the same parameters every 10 ms
        self.exitButton.after(40, partial(self.button_animation, passes, bigPasses, maxPasses, button, endCommand, btnText, animateeLeft, animateeRight, animationDirection))



main = MainMenu()
main.open_menu()

# Prevents menu from disappearing when shop is opened
root.grid_rowconfigure(0, weight=1)

# userGrid = grid.Grid(10, root = root, colors=colors)
# userGrid.generate()
# userGrid.start_ship_placement()



root.mainloop()