from functools import partial
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import os
import time

import game
import shop as shopFile
from warships import countries, countryColors

# (Supposed to) read country from persistent storage (not implemented yet)
country = 'United States'

# Color theme

colorSetting = 'dark'

if colorSetting == 'light':
    color = '#ddd'
    textColor = '#000'
    accentColor1 = '#ccc'
    accentColor2 = '#bbb'
elif colorSetting == 'dark':
    color = '#222'
    textColor = '#fff'
    accentColor1 = '#333'
    accentColor2 = '#444'
else: # Else statement purely to avoid PyCharm warnings
    color = '#000'
    textColor = '#000'
    accentColor1 = '#000'
    accentColor2 = '#000'

countryColor = countryColors[country][0]

colors = list((color, textColor, accentColor1, accentColor2, countryColor))

# Window specs

root = Tk()
root.geometry('1400x1000')
root.title('Battleships')
root.configure(bg=color, border=25)
root.resizable(False, False)

# Font specs

fontPath = os.path.join(os.getcwd(), 'Inter.ttf')
font.Font(root=root, name='Inter', size=10)

defaultFont = font.nametofont('TkDefaultFont')
defaultFont.configure(family='Inter', size=10)

# Main menu window

class MainMenu:
    def __init__(self):

        # Load external instances
        self.shopObj = shopFile.Shop(root=root, country=country, colors=colors)
        self.gameObj = game.Game(root=root, colors=colors)
        self.shopOpened = False

    # Changes the active country
    def changeCountry(self, newCountry):
        global country, countryColor, colors
        country = newCountry
        countryColor = countryColors[country][0]
        colors[4] = countryColor
        print(newCountry)

        # Regenerates the menu with the new country's color theme, also re-creates the shop for the specified country
        self.shopObj = shopFile.Shop(root=root, country=country, colors=colors)
        self.open_menu()

    def open_menu(self):

        # Overall frame for the main menu
        self.menuFrame = Frame(root, bg=color, padx=100)
        self.menuFrame.grid(column=0, row=0)

        # Label for game title (will look better later)
        titleLabel = Label(self.menuFrame, text='Battleships', font=('Inter', 50, 'bold'), padx=50, pady=20,
                           fg=textColor, bg=color)
        titleLabel.grid(column=0, row=0, pady=20, sticky='nsew')

        # Play button
        self.playButton = Button(self.menuFrame, text='>>   Embark   <<', font=('Inter', 20, 'bold'), padx=5, pady=20,
                                 fg='white', bg=countryColor, relief='groove', command=self.opening_game) # This passes the actual command to a later function so that the button is defined
        self.playButton.grid(column=0, row=1, sticky='nsew')

        # Shop button
        self.shopButton = Button(self.menuFrame, text='Shop', font=('Inter', 20), padx=0, pady=20, fg='white', bg=countryColor, relief='groove', command=self.open_shop)
        self.shopButton.grid(column=0, row=2, sticky='ew')

        # Flag buttons
        '''
        self.flagButtonFrame = Frame(root, bg=color, padx=50, pady=10)
        self.flagButtonFrame.grid(column=1, row=0)
        for i, country in enumerate(countryColors.items()):
            rszdImg = country[1][1]
            rszdImg.thumbnail([100, 100])
            tkImg = ImageTk.PhotoImage(rszdImg)
            flagButton = Button(self.flagButtonFrame, image=tkImg, bg=textColor, relief="groove", command=lambda newCountry=country: self.changeCountry(newCountry[0]))
            flagButton.image = tkImg
            flagButton.grid(column=0, row=i, sticky='ew', padx=10, pady=10)
            flagLabel = Label(self.flagButtonFrame, text=country[0], font=('Inter', 14, 'bold'), bg=color, fg=textColor, padx=10)
            flagLabel.grid(column=1, row=i, sticky='w')
        '''

        # Exit button
        self.exitButton = Button(self.menuFrame, text='<<  Deboard  >>', font=('Inter', 20), padx=5, pady=20,
                                 fg='white', bg=countryColor, activebackground='#db4040', activeforeground='white', relief='groove', command=self.closing_game)
        self.exitButton.grid(column=0, row=3, sticky='ew')

        # Checker for aborting an animated button, flipped if abort button is pressed
        self.abort = False


    # Initiates game opening
    def opening_game(self):
        self.button_animation(15, 0, 0, self.playButton, 'self.open_game', 'Embarking', '>>', '<<', -1, 15)

    def open_game(self):
        # Kills existing non-game stuff
        self.menuFrame.destroy()

        try: # Closes the shop if it was ever created
            self.shopObj.shopFrame.destroy()
        except:
            print('shop never opened')
        # self.flagButtonFrame.destroy()
        root.grid_rowconfigure(0, weight=0)
        self.gameObj.start()


    # Opens shop
    def open_shop(self):

        # Opens the shop and checks for owned ships
        self.shopObj.open()
        self.shopObj.check_ships()

        # Sets the shop button to close it when pressed
        self.shopButton.config(relief='sunken', command=self.reopen_menu)

    # Reopens the main menu after closing the shop
    def reopen_menu(self):

        # Closes shop
        self.shopObj.shopFrame.destroy()

        # Resets shop button
        self.shopButton.config(relief='groove', command=self.open_shop)

    # Aborts game close if the close button is pressed during the animation
    def abort_game_close(self):
        self.abort = True
        self.exitButton.config(text='<<  Deboard  >>', font=('Inter', 20), padx=5, pady=20,
                               fg='white', bg=countryColor, activebackground='#db4040', activeforeground='white', relief='groove', command=self.closing_game)

    # Prepares to close the game
    def closing_game(self):

        self.abort = False # Sets checker to true again

        # Sets exit button to an abort button
        self.exitButton.config(text='<<  Abort  >>', bg='#db4040', activebackground='#db4040', activeforeground='white',
                               relief='sunken', command=self.abort_game_close)

        # Starts the closing button animation
        (self.button_animation
         (0, 0, 18, self.exitButton, 'root.destroy', 'Abort', '<<', '>>', 1, 0))

    # Animation for any button that has arrows
    def button_animation(self, passes, bigPasses, maxPasses, button, endCommand, btnText, animateeLeft, animateeRight, animationDirection, startPasses):

        # Adds a space to the abort button string
        spaces = ' ' * passes

        # Checks if the end command should be executed or aborted
        if bigPasses == 3 and not self.abort: # Number of cycles before the end command is executed
            eval(f'{endCommand}()') # Evaluates the end command of the button animation
            return None
        elif self.abort: # Stops the function if the abort button is pressed
            return None

        # Updates the abort button string
        button.config(text=f'{animateeLeft}{spaces}  {btnText}  {spaces}{animateeRight}')

        # Updates the number of passes
        passes += animationDirection # Positive 1 moves the arrows away from the text, negative 1 moves them towards the text
        print(passes) # Test
        if passes == maxPasses: # Number of passes before the number of spaces are reset
            bigPasses += 1
            passes = startPasses # Resets passes to original value

        # Animation that re-runs the function with all the same parameters every 10 ms
        (self.exitButton.after
         (40, partial(self.button_animation, passes, bigPasses, maxPasses, button, endCommand, btnText, animateeLeft, animateeRight, animationDirection, startPasses)))


main = MainMenu()
main.open_menu()

# Prevents menu from disappearing when shop is opened
root.grid_rowconfigure(0, weight=1)

# userGrid = grid.Grid(10, root = root, colors=colors)
# userGrid.generate()
# userGrid.start_ship_placement()


root.mainloop()