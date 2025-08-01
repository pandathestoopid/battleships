import time
from tkinter import *
from PIL import ImageTk, Image
from functools import partial

import warships
import drydock

points = 10000


# Scrollable frame class
class ScrollFrame(Frame):
    def __init__(self, container, bg, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = Canvas(self, borderwidth=0, bg=bg, highlightthickness=0, width=800, height=600)
        self.scrollbar = Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scrollableFrame = Frame(self.canvas, bg=bg)

        self.scrollableFrame.bind(
            '<Configure>',
            lambda e: self.canvas.configure(scrollregion=(self.canvas.bbox('all')))
        )

        self.canvas.create_window((0,0), window=self.scrollableFrame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side='left', fill='both', expand=True)
        self.scrollbar.pack(side='right', fill='y')

        self.canvas.bind('<MouseWheel>', self.mouse_scroll)

    def mouse_scroll(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), 'units')


# The shop class
class Shop:
    def __init__(self, root, country, colors):

        # GUI constructor
        self.root = root
        self.color = colors[0]
        self.textColor = colors[1]
        self.accentColor1 = colors[2]
        self.accentColor2 = colors[3]

        # Country the player is shopping for
        self.country = country

        # Unpacks all ships
        self.ships = warships.ships

        # Determines which country the user is shopping for, then sends that as an index to the ship class dictionary
        countryIndex = warships.countries.index(self.country)

        # Unpacks the ship class lists for the desired country
        self.caListings = self.ships[0]['ships'][countryIndex]
        self.baListings = self.ships[1]['ships'][countryIndex]
        self.deListings = self.ships[2]['ships'][countryIndex]
        self.subListings = self.ships[3]['ships'][countryIndex]
        self.frListings = self.ships[4]['ships'][countryIndex]

        # Re-packs them into lists for easier iteration in the shop window
        self.listings = [self.caListings, self.baListings, self.deListings, self.subListings, self.frListings]
        self.classNames = ['Carriers', 'Battleships', 'Destroyers', 'Submarines', 'Frigates']
        self.levelNames = ['Basic', 'Standard', 'Enhanced', 'Superior']

        # List of dictionaries for button states (for easier customization), commands cannot be listed here due to situational requirements

        buy = { # The standard button showing default, not-yet-interacted-with elements
            'text': 'Buy',
            'color': warships.countryColors[self.country],
            'relief': 'flat'
        }

        declined = {
            'text': 'Declined',
            'color': '#db4040'
        }

        confirm = {
            'text': 'Confirm',
            'color': warships.countryColors[self.country],
            'relief': 'flat'
        }

        owned = {
            'text': 'Owned',
            'color': 'Green',
            'relief': 'flat'
        }

        equipped = {
            'text': 'Equipped',
            'color': 'Green',
            'relief': 'sunken'
        }

        self.buttonStates = [buy, declined, confirm, owned, equipped]


    # Opens the shop window
    def open(self):

        # Shop frame
        self.shopFrame = Frame(self.root, bg=self.accentColor1)
        self.shopFrame.grid(column=1, row=0, padx=10, pady=10)

        # Title, framed with three labels for aesthetic purposes
        titleFrame = Frame(self.shopFrame, bg=self.accentColor1)
        titleFrame.grid(column=0, row=0, padx=10, pady=10, sticky='w')
        titleLabel1 = Label(titleFrame, text=f'Shop for', font=('Inter', 20, 'bold'), bg=self.accentColor1, fg=self.textColor)
        titleLabel1.grid(column=0, row=0, sticky='w')
        titleLabel2 = Label(titleFrame, text=f'{self.country}', font=('Inter', 20, 'bold'), bg=warships.countryColors[self.country], fg='white')
        titleLabel2.grid(column=1, row=0, sticky='w')
        titleLabel3 = Label(titleFrame, text=f'ships', font=('Inter', 20, 'bold'), bg=self.accentColor1, fg=self.textColor)
        titleLabel3.grid(column=2, row=0, sticky='w')

        # Points available counter, framed with two labels for aesthetic purposes
        pointsFrame = Frame(self.shopFrame, bg=self.accentColor1)
        pointsFrame.grid(column=0, row=1, padx=10, pady=10, sticky='w')
        self.pointsAvailable = Label(pointsFrame, text=f'Points Available:  {points}', font=('Inter', 14, 'bold'), bg=self.accentColor1, fg=self.textColor)
        self.pointsAvailable.grid(column=0, row=1, sticky='w')
        pointsCurrency = Label(pointsFrame, text='P', font=('Inter', 14, 'bold'), fg='#006abb', bg=self.accentColor1)
        pointsCurrency.grid(column=1, row=1, sticky='w')

        scrollFrame = ScrollFrame(self.shopFrame, bg=self.accentColor1)
        scrollFrame.grid(column=0, row=2, padx=10, pady=10, sticky='w')

        listingsFrame = scrollFrame.scrollableFrame

        # 2D list of buttons for the shop for referencing

        self.shopButtons = [[None for _ in range(len(self.classNames) * len(self.levelNames))] for _ in range(len(self.classNames) * len(self.levelNames))]

        for c, shipClass in enumerate(self.listings):

            # Generates labels for the ship classes on sale
            classLabel = Label(listingsFrame, text=f'{self.classNames[c].upper()} \u2198', font=('Inter', 12, 'bold'), padx=5, pady=10, bg=self.accentColor1, fg=self.textColor, anchor='w')
            classLabel.grid(column=0, row=self.listings.index(shipClass)*2, sticky='w')

            # Generates a frame for the below listings for each class
            classFrame = Frame(listingsFrame, bg=self.accentColor1)
            classFrame.grid(column=0, row=self.listings.index(shipClass)*2+1, sticky='w')

            for s, ship in enumerate(shipClass):

                # Listing cards for each ship
                shipFrame = Frame(classFrame, padx=15, pady=5, relief='flat', bg=self.accentColor1, bd=0)
                shipFrame.grid(column=s, row=0, sticky='w')

                # Name of the ship with some slight changes to the name string for aesthetic purposes
                prefix, name = ship['name'].split(' ', 1)
                shipName = Label(shipFrame, text=f'{prefix}\n{name}', font=('Inter', 10, 'bold'), padx=5, pady=5, anchor='w', justify='left', bg=self.accentColor1, fg=self.textColor)
                shipName.grid(column=0, row=1, sticky='w')

                # Image of the ship
                img = Image.open(f'assets/ships/{ship['name']}.jpg')
                tkImg = ImageTk.PhotoImage(img)
                shipImage = Label(shipFrame, image=tkImg, padx=1, pady=1)
                shipImage.image = tkImg
                shipImage.grid(column=0, row=0, sticky='w')

                # Level of the ship
                shipLevel = Label(shipFrame, text=f'Level {ship['level']}\n{self.levelNames[ship['level']]}', padx=5, pady=5, anchor='w', justify='left', bg=self.accentColor1, fg=self.textColor)
                shipLevel.grid(column=0, row=2, sticky='w')

                # Frame for the price which has two separate labels for aesthetic purposes
                shipPriceFrame = Frame(shipFrame, padx=5, pady=5, bg=self.accentColor1)
                shipPriceFrame.grid(column=0, row=3, sticky='w')

                # Price of the ship
                shipPrice = Label(shipPriceFrame, text=f'{200*ship['level']**3}', bg=self.accentColor1, fg=self.textColor)
                shipPrice.grid(column=0, row=0, sticky='w')

                # Currency symbol
                shipCurrency = Label(shipPriceFrame, text='P', font=('Inter', 11, 'bold'), fg='#006abb', bg=self.accentColor1)
                shipCurrency.grid(column=1, row=0, sticky='w')

                # Buy button
                shipBuy = Button(
                    shipFrame, text='Buy', bg=warships.countryColors[self.country], fg='White', font=('Inter', 11, 'bold'), padx=20, relief='flat',
                    command=lambda price=(200*ship['level']**3), shopShip=s, shopClass=c: self.confirm_purchase(price, shopShip, shopClass)
                )
                shipBuy.grid(column=0, row=4, sticky='ew')

                # Space between next row
                spaceRow = Label(shipFrame, text='', padx=5, pady=5, bg=self.accentColor1, fg=self.textColor)
                spaceRow.grid(column=0, row=5)

                # Append button to 2D list for referencing
                self.shopButtons[c][s] = shipBuy

    def confirm_purchase(self, price, shopShip, shopClass):
        if points < price:
            self.update_button(shopClass, shopShip, 'Declined', '#db4040', 'sunken', self.strawman)
        else:
            self.update_button(shopClass, shopShip, 'Confirm', warships.countryColors[self.country], 'sunken', partial(self.buy, price, shopShip, shopClass))
        pass

    def buy(self, price, shopShip, shopClass):

        # Purchase ship
        global points
        points -= price
        self.update_button(shopClass, shopShip, 'Owned', 'Green', 'flat', partial(self.equip_ship, shopShip, shopClass))

        # Updates points available counter
        self.pointsAvailable.config(text=f'Points Available:  {points}')

        # Adds ship to owned ships list in drydock.py
        drydock.ownedShips.append(self.listings[shopClass][shopShip])

    # Updates the button with the desired text and color and stuff based on what action was taken
    def update_button(self, shopClass, shopShip, msg, color, relief, command):
        self.shopButtons[shopClass][shopShip].config(text=msg, bg=color, fg='White', activeforeground='White', relief=relief, command=command)

    def equip_ship(self, shopShip, shopClass):

        print(f'Ship: {shopShip}, Class: {shopClass}')

        # Gets the previously equipped ship
        prevShip = drydock.equippedShips[shopClass]
        if prevShip is not None and prevShip != shopShip:
            self.update_button(shopClass, prevShip, 'Owned', 'Green', 'flat', partial(self.equip_ship, prevShip, shopClass))

        print(f'Button removed - Class: {shopClass}, Ship: {drydock.equippedShips[shopClass]} - With command to equip ship {shopShip} and class {shopClass}')

        # Adds ship to the equipped ships list in drydock.py
        drydock.equippedShips[shopClass] = shopShip

        print(f'Equipped ship {shopShip}, Class: {shopClass}')

        # Button reflects new ship
        self.update_button(shopClass, shopShip, 'Equipped', 'Green', 'ridge', self.strawman)

        print(drydock.equippedShips)


    # Check if ships are already owned or equipped
    def check_ships(self):
        for c, shipClass in enumerate(self.listings):
            for s, ship in enumerate(shipClass):
                if s == drydock.equippedShips[c]:
                    self.shopButtons[c][s].config(text='Equipped', bg='Green', fg='White', relief='ridge', activebackground='Green',
                                                  activeforeground='White', command=self.strawman)
                elif ship in drydock.ownedShips:
                    self.shopButtons[c][s].config(text='Owned', bg='Green', fg='White', relief='flat',
                                                  activebackground='Green', command=partial(self.equip_ship, s, c))

    # Button command for soft-disabled ones
    def strawman(self):
        pass