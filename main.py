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
                            fg='white', bg='#006abb', relief='groove', command=self.animate_play)
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
                            fg='white', bg='#006abb',activebackground='#db4040', activeforeground='white', relief='groove', command=self.close_game)
        self.exitButton.grid(column=0, row=3, sticky='ew')

        # Checker for closing the game, flipped if abort button is pressed
        self.close = True


    def animate_play(self):

        # Work in progress
        for space in range(-25):
            spaces = ' '*space

        self.playButton.config(text=f'>>{spaces}Embark{spaces}<<')

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
        self.close = False
        self.exitButton.config(text='<<  Deboard  >>', font=('Inter', 20), padx=5, pady=20,
                            fg='white', bg='#006abb',activebackground='#db4040', activeforeground='white', relief='groove', command=self.close_game)

    # Actually closes game
    def destroy_game(self):
        if self.close:
            root.destroy()

    # Prepares to close the game
    def close_game(self):

        self.close = True # Sets checker to true again
        self.closePasses = 0 # Defines passes
        self.bigClosePasses = 0 # Defines big passes

        # Sets exit button to an abort button
        self.exitButton.config(text='<<  Abort  >>', bg='#db4040', activebackground='#db4040', activeforeground='white',
                               relief='sunken', command=self.abort_game_close)

        # Starts the closing button animation
        self.close_game_animation()

    # Animation for closing the game, this can be made more efficient but I'm too tired to do that rn
    def close_game_animation(self):

        # Adds a space to the abort button string
        spaces = ' ' * self.closePasses

        # Checks if the game should be closed or closing process should be aborted
        if self.bigClosePasses == 5 and self.close: # Number of cycles before the game is closed
            self.destroy_game()
            return None
        elif not self.close: # Stops the function if the abort button is pressed
            return None

        # Updates the abort button string
        self.exitButton.config(text=f'<<{spaces}  Abort  {spaces}>>')

        # Animation that re-runs the function every 10 ms
        self.exitButton.after(40, self.close_game_animation)

        # Updates the number of passes
        self.closePasses += 1
        if self.closePasses == 18: # Number of passes before the number of spaces are reset
            self.bigClosePasses += 1
            self.closePasses = 0



main = MainMenu()
main.open_menu()

# Prevents menu from disappearing when shop is opened
root.grid_rowconfigure(0, weight=1)

# userGrid = grid.Grid(10, root = root, colors=colors)
# userGrid.generate()
# userGrid.start_ship_placement()



root.mainloop()