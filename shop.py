from operator import index
from tkinter import *
from PIL import ImageTk, Image
from functools import partial

import warships

points = 10000

class Shop:
    def __init__(self, root, country):

        # GUI constructor
        self.root = root

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
        shopFrame = Frame(self.root, bg='white')
        shopFrame.grid(column=1, row=0, padx=10, pady=10)

        # Title, framed with three labels for aesthetic purposes
        titleFrame = Frame(shopFrame, bg='white')
        titleFrame.grid(column=0, row=0, padx=10, sticky='w')
        titleLabel1 = Label(titleFrame, text=f'Shop for', font=('Inter', 12, 'bold'), bg='white')
        titleLabel1.grid(column=0, row=0, sticky='w')
        titleLabel2 = Label(titleFrame, text=f'{self.country}', font=('Inter', 12, 'bold'), bg=warships.countryColors[self.country], fg='white')
        titleLabel2.grid(column=1, row=0, sticky='w')
        titleLabel3 = Label(titleFrame, text=f'ships', font=('Inter', 12, 'bold'), bg='white')
        titleLabel3.grid(column=2, row=0, sticky='w')

        # Points available counter, framed with two labels for aesthetic purposes
        pointsFrame = Frame(shopFrame, bg='white')
        pointsFrame.grid(column=0, row=1, padx=10, pady=10, sticky='w')
        self.pointsAvailable = Label(pointsFrame, text=f'Points Available:  {points}', font=('Inter', 11, 'bold'), bg='white')
        self.pointsAvailable.grid(column=0, row=1, sticky='w')
        pointsCurrency = Label(pointsFrame, text='P', font=('Inter', 11, 'bold'), fg='#00008B', bg='white')
        pointsCurrency.grid(column=1, row=1, sticky='w')

        listingsFrame = Frame(shopFrame)
        listingsFrame.grid(column=0, row=2, padx=10, pady=10, sticky='w')

        # Dictionary of buttons for the shop for referencing

        self.shopButtons = [[None for _ in range(len(self.classNames) * len(self.levelNames))] for _ in range(len(self.classNames) * len(self.levelNames))]

        for i, shipClass in enumerate(self.listings):

            # Generates labels for the ship classes on sale
            classLabel = Label(listingsFrame, text=self.classNames[i].upper(), font=('Inter', 10, 'bold'), padx=5, pady=10)
            classLabel.grid(column=0, row=self.listings.index(shipClass)*2, sticky='w')

            # Generates frame for the below listings for each class
            classFrame = Frame(listingsFrame)
            classFrame.grid(column=0, row=self.listings.index(shipClass)*2+1, sticky='w')

            for c, ship in enumerate(shipClass):

                # Listing cards for each ship
                shipFrame = Frame(classFrame, bg='#eee', padx=15, pady=5, relief='ridge')
                shipFrame.grid(column=c, row=0, sticky='w')

                # Name of the ship with some slight changes to the name string for aesthetic purposes
                prefix, name = ship['name'].split(' ', 1)
                shipName = Label(shipFrame, text=f'{prefix}\n{name}', font=('Inter', 10, 'bold'), padx=5, pady=5, anchor='w', justify='left')
                shipName.grid(column=0, row=1, sticky='w')

                # Image of the ship
                img = Image.open(f'assets/ships/{ship['name']}.jpg')
                tkImg = ImageTk.PhotoImage(img)
                shipImage = Label(shipFrame, image=tkImg, padx=2, pady=5)
                shipImage.image = tkImg
                shipImage.grid(column=0, row=0, sticky='w')

                # Level of the ship
                shipLevel = Label(shipFrame, text=f'Level {ship['level']}\n{self.levelNames[ship['level']]}', padx=5, pady=5, anchor='w', justify='left')
                shipLevel.grid(column=0, row=2, sticky='w')

                # Frame for the price which has two seperate labels for aethestic purposes
                shipPriceFrame = Frame(shipFrame, padx=5, pady=5)
                shipPriceFrame.grid(column=0, row=3, sticky='w')

                # Price of the ship
                shipPrice = Label(shipPriceFrame, text=f'{200*ship['level']**3}')
                shipPrice.grid(column=0, row=0, sticky='w')

                # Currency symbol
                shipCurrency = Label(shipPriceFrame, text='P', font=('Inter', 11, 'bold'), fg='#00008B')
                shipCurrency.grid(column=1, row=0, sticky='w')

                # Buy button
                shipBuy = Button(
                    shipFrame, text='Buy', bg='Blue', fg='White', font=('Inter', 11, 'bold'), padx=20, activebackground='Light blue', relief='ridge',
                    command=lambda price=(200*ship['level']**3), shopShip=c, shopClass=i: self.confirm_purchase(price, shopShip, shopClass)
                )
                shipBuy.grid(column=0, row=4, sticky='ew')

                # Space between next row
                spaceRow = Label(shipFrame, text='', padx=5, pady=5)
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
        global points
        points -= price
        self.shopButtons[shopClass][shopShip].config(text='Owned', bg='Green', activebackground='#88e788', activeforeground='White', command=partial(self.equip_ship, shopShip, shopClass))
        self.pointsAvailable.config(text=f'Points Available:  {points}')
        print(points)

    def equip_ship(self, shopShip, shopClass):
        self.shopButtons[shopClass][shopShip].config(text='Equipped', bg='Green', fg='White', command=partial(self.equip_ship, shopShip, shopClass))
