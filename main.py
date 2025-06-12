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

        print('opening menu')

        # Overall frame for the main menu
        self.menuFrame = Frame(root, bg=color, padx=525, pady=100)
        self.menuFrame.grid(column=0, row=0)

        # Label for game title (will look better later)
        titleLabel = Label(self.menuFrame, text='Battleships', font=('Inter', 50, 'bold'), padx=50, pady=100, fg='#006abb', bg=color, anchor='center', justify='center')
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
        shopButton = Button(shipCustomizeFrame, text='Shop', font=('Inter', 20), padx=78, pady=20, fg='white', bg='#006abb', relief='groove', command=self.open_shop)
        shopButton.grid(column=1, row=0, sticky='ew')

        # Exit button
        self.exitButton = Button(self.menuFrame, text='<<  Deboard  >>', font=('Inter', 20), padx=5, pady=20,
                            fg='white', bg='#006abb',activebackground='#db4040', activeforeground='white', relief='groove')
        self.exitButton.grid(column=0, row=3, sticky='ew')


    def animate_play(self):


        # Work in progress
        for space in range(-25):
            spaces = ' '*space
            self.playButton.config(text=f'>>{spaces}Embark{spaces}<<')

    def open_shop(self):
        self.menuFrame.destroy()
        shopObj.open()

        self.backButton = Button(root, text='\u2190', font=('Inter', 20, 'bold'), bg=accentColor1, fg=textColor, padx=10, pady=10, relief='flat',
                            activebackground=accentColor2, activeforeground=textColor, bd=0, command=self.reopen_menu)
        self.backButton.grid(column=0, row=0, padx=10, pady=10, sticky='n')

    def reopen_menu(self):
        shopObj.shopFrame.destroy()
        self.backButton.destroy()
        self.open_menu()


main = MainMenu()
main.open_menu()

# Grid routine, going to put into something else soon

# userGrid = grid.Grid(10, root = root, colors=colors)
# userGrid.generate()
# userGrid.start_ship_placement()



root.mainloop()