from tkinter import *
from PIL import ImageTk, Image
from functools import partial

import warships
import drydock

points = 10000

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

        listingsFrame = Frame(self.shopFrame, bg=self.accentColor1)
        listingsFrame.grid(column=0, row=2, padx=10, pady=10, sticky='w')

        # 2D list of buttons for the shop for referencing

        self.shopButtons = [[None for _ in range(len(self.classNames) * len(self.levelNames))] for _ in range(len(self.classNames) * len(self.levelNames))]

        for i, shipClass in enumerate(self.listings):

            # Generates labels for the ship classes on sale
            classLabel = Label(listingsFrame, text=f'{self.classNames[i].upper()} \u2198', font=('Inter', 12, 'bold'), padx=5, pady=10, bg=self.accentColor1, fg=self.textColor, anchor='w')
            classLabel.grid(column=0, row=self.listings.index(shipClass)*2, sticky='w')

            # Generates frame for the below listings for each class
            classFrame = Frame(listingsFrame, bg=self.accentColor1)
            classFrame.grid(column=0, row=self.listings.index(shipClass)*2+1, sticky='w')

            for c, ship in enumerate(shipClass):

                # Listing cards for each ship
                shipFrame = Frame(classFrame, padx=15, pady=5, relief='flat', bg=self.accentColor1, bd=0)
                shipFrame.grid(column=c, row=0, sticky='w')

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

                # Frame for the price which has two seperate labels for aethestic purposes
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
                    shipFrame, text='Buy', bg=warships.countryColors[self.country], fg='White', font=('Inter', 11, 'bold'), padx=20, activebackground='Light blue', relief='flat',
                    command=lambda price=(200*ship['level']**3), shopShip=c, shopClass=i: self.confirm_purchase(price, shopShip, shopClass)
                )
                shipBuy.grid(column=0, row=4, sticky='ew')

                # Space between next row
                spaceRow = Label(shipFrame, text='', padx=5, pady=5, bg=self.accentColor1, fg=self.textColor)
                spaceRow.grid(column=0, row=5)

                # Append button to 2D list for referencing
                self.shopButtons[i][c] = shipBuy

    def confirm_purchase(self, price, shopShip, shopClass):
        if points < price:
            self.shopButtons[shopClass][shopShip].config(text='Declined', bg='Red', activebackground='#ff6c70', activeforeground='White')
        else:
            self.shopButtons[shopClass][shopShip].config(text='Confirm', command=partial(self.buy, price, shopShip, shopClass))
        pass

    def buy(self, price, shopShip, shopClass):

        # Purchases ship
        global points
        points -= price
        self.shopButtons[shopClass][shopShip].config(text='Owned', bg='Green', activebackground='#88e788', activeforeground='White', relief='flat',
                                                     command=partial(self.equip_ship, shopShip, shopClass))

        # Updates points available counter
        self.pointsAvailable.config(text=f'Points Available:  {points}')

        # Adds ship to owned ships list in drydock.py
        drydock.ownedShips.append(self.listings[shopClass][shopShip])

    # Updates the button with the desired text and color and stuff based on what action was taken
    def update_button(self, shopClass, shopShip, msg, color, clickColor, relief):
        self.shopButtons[shopClass][shopShip].config(text=msg, bg=color, activebackground=clickColor, activeforeground='White', relief=relief,)

    def equip_ship(self, shopShip, shopClass):

        # Removes other equipped ships of the same class
        # drydock.equippedShips = [ship for ship in drydock.equippedShips if self.listings[shopClass].index(ship) != shopShip]



        # Equips ship
        self.shopButtons[shopClass][shopShip].config(text='Equipped', bg='Green', fg='White', relief='ridge', activebackground='Green',
                                                     command=self.strawman)

        # Adds ship to equipped ships list in drydock.py
        drydock.equippedShips.append(self.listings[shopClass][shopShip])
        # print(drydock.equippedShips)
        for ship in drydock.equippedShips:
            if self.listings[shopClass].index(ship) != shopShip:
                drydock.equippedShips.remove(ship)

            print(f'Equipped ship: {self.listings[shopClass].index(ship)}, Bought ship: {shopShip}')

    # Check if ships are already owned or equipped
    def check_ships(self):
        for i, shipClass in enumerate(self.listings):
            for c, ship in enumerate(shipClass):
                if ship in drydock.equippedShips:
                    self.shopButtons[i][c].config(text='Equipped', bg='Green', fg='White', relief='ridge', activebackground='Green',
                                              activeforeground='White', command=self.strawman)
                elif ship in drydock.ownedShips:
                    self.shopButtons[i][c].config(text='Owned', bg='Green', fg='White', relief='flat',
                                                  activebackground='Green', command=partial(self.equip_ship, c, i))

    # Button command for soft-disabled ones
    def strawman(self):
        pass