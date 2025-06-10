from operator import index
from tkinter import *
from PIL import ImageTk, Image

import warships

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

        # Shop interface
        shopLabel = Label(self.root, text=f'Shop for {self.country} ships')
        shopLabel.grid(column=2, row=0, padx=10, pady=10, sticky='w')
        shopFrame = Frame(self.root)
        shopFrame.grid(column=2, row=1, padx=10, pady=10, sticky='w')

        # Test for images
        self.listings = self.caListings

        for i, shipClass in enumerate(self.listings):

            # Generates labels for the ship classes on sale
            classLabel = Label(shopFrame, text=self.classNames[i].upper(), font=('Inter', 10, 'bold'), padx=5, pady=10)
            classLabel.grid(column=0, row=self.listings.index(shipClass)*2, sticky='w')

            # Generates frame for the below listings for each class
            classFrame = Frame(shopFrame)
            classFrame.grid(column=0, row=self.listings.index(shipClass)*2+1, sticky='w')

            for c, ship in enumerate(shipClass):

                # Creates listing cards for each ship
                shipFrame = Frame(classFrame, bg='#eee')
                shipFrame.grid(column=c, row=0, sticky='w')

                # Ship's image (will implement later)
                print(ship)
                # img = Image.open(f'assets/ships/{ship['name']}.jpg')
                # tkImg = ImageTk.PhotoImage(img)
                # shipImage = Label(shipFrame, image=tkImg, padx=2, pady=5)
                # shipImage.image = tkImg
                # shipImage.grid(column=0, row=0, sticky='w')

                # Label for name of the ship
                shipName = Label(shipFrame, text=ship['name'], font=('Inter', 10, 'bold'), padx=5, pady=5)
                shipName.grid(column=0, row=1, sticky='w')

                # Label for level of the ship
                shipLevel = Label(shipFrame, text=self.levelNames[ship['level']], padx=5, pady=5)
                shipLevel.grid(column=0, row=2, sticky='w')

                # Frame for the price which has two seperate labels for aethestic purposes
                shipPriceFrame = Frame(shipFrame, padx=5, pady=5)
                shipPriceFrame.grid(column=0, row=3, sticky='w')

                # Label for price of the ship
                shipPrice = Label(shipPriceFrame, text=f'{200*ship['level']**3}')
                shipPrice.grid(column=0, row=0, sticky='w')

                # Label for the currency symbol of the ship
                shipCurrency = Label(shipPriceFrame, text='P', font=('Inter', 11, 'bold'), fg='Midnight blue')
                shipCurrency.grid(column=1, row=0, sticky='w')

                # Buy button
                shipBuy = Button(shipFrame, text='Buy', bg='Blue', fg='White', font=('Inter', 11, 'bold'), padx=20, activebackground='Light blue', command=self.buy)
                shipBuy.grid(column=0, row=4)

                # Space between next row
                spaceRow = Label(shipFrame, text='', padx=5, pady=5)
                spaceRow.grid(column=0, row=5)

    def buy(self):
        print('cha-ching')
        pass