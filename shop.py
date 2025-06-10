from operator import index
from tkinter import *

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

    # Opens the shop window
    def open(self):

        # Shop interface
        shopLabel = Label(self.root, text=f'Shop for {self.country} ships')
        shopLabel.grid(column=2, row=0, padx=10, pady=10, sticky='w')
        shopFrame = Frame(self.root)
        shopFrame.grid(column=2, row=1, padx=10, pady=10, sticky='w')

        for i, shipClass in enumerate(self.listings):

            # Generates labels for the ship classes on sale
            classLabel = Label(shopFrame, text=self.classNames[i].upper(), font=('Inter', 10, 'bold'))
            classLabel.grid(column=0, row=self.listings.index(shipClass)*2, sticky='w')

            # Generates frame for the below listings for each class
            classFrame = Frame(shopFrame)
            classFrame.grid(column=0, row=self.listings.index(shipClass)*2+1, sticky='w')

            for c, ship in enumerate(shipClass):

                # Creates listing cards for each ship
                shipFrame = Frame(classFrame)
                shipFrame.grid(column=c, row=0, sticky='w')
                shipName = Label(shipFrame, text=ship['name'], font=('Inter', 10, 'bold'))
                shipName.grid(column=0, row=0, sticky='w')
                shipPrice = Label(shipFrame, text=f'${ship["price"]}', font=('Inter', 10, 'bold'))
                shipPrice.grid(column=1, row=0, sticky='w')