from random import *
from weapons import *

# All types of ships

carriersType = {
    'name': 'Aircraft Carrier',
    'size': 5,
    'armament': 'fighters',
    'torp acc': 90,
    'torp instaSink': 5
}

# Carrier ship names

kittyHawk = {
    'name': 'USS Kitty Hawk',
    'nation': 'United States',
    'level': 0,
    'type': 'carrier'
}

enterprise = {
    'name': 'USS Enterprise',
    'nation': 'United States',
    'level': 1,
    'type': 'carrier'
}

nimitz = {
    'name': 'Nimitz',
    'nation': 'United States',
    'level': 2,
    'type': 'carrier'
}

ford = {
    'name': 'Ford',
    'nation': 'United States',
    'level': 3,
    'type': 'carrier'
}

# Battleship names

washington = {
    'name': 'USS Washington',
    'nation': 'United States',
    'level': 0,
    'type': 'battleship'
}

north_carolina = {
    'name': 'USS North Carolina',
    'nation': 'United States',
    'level': 1,
    'type': 'battleship'
}

wisconson = {
    'name': 'USS Wisconsin',
    'nation': 'United States',
    'level': 2,
    'type': 'battleship'
}

montana = {
    'name': 'USS Montana',
    'nation': 'United States',
    'level': 3,
    'type': 'battleship'
}

# Destroyer names

decatur = {
    'name': 'USS Decatur',
    'nation': 'United States',
    'level': 0,
    'type': 'destroyer'
}

fletcher = {
    'name': 'USS Fletcher',
    'nation': 'United States',
    'level': 1,
    'type': 'destroyer'
}

spruance = {
    'name': 'USS Spruance',
    'nation': 'United States',
    'level': 2,
    'type': 'destroyer'
}

intrepid = {
    'name': 'USS Intrepid',
    'nation': 'United States',
    'level': 3,
    'type': 'destroyer'
}

# Submarine names

nautilus = {
    'name': 'USS Nautilus',
    'nation': 'United States',
    'level': 0,
    'type': 'submarine'
}

losAngeles = {
    'name': 'USS Los Angeles',
    'nation': 'United States',
    'level': 1,
    'type': 'submarine'
}

seawolf = {
    'name': 'USS Seawolf',
    'nation': 'United States',
    'level': 2,
    'type': 'submarine'
}

wahoo = {
    'name': 'USS Wahoo',
    'nation': 'United States',
    'level': 3,
    'type': 'submarine'
}

# Frigate names

knox = {
    'name': 'USS Knox',
    'nation': 'United States',
    'level': 0,
    'type': 'frigate'
}

brooke = {
    'name': 'USS Brooke',
    'nation': 'United States',
    'level': 1,
    'type': 'frigate'
}

independence = {
    'name': 'USS Independence',
    'nation': 'United States',
    'level': 2,
    'type': 'frigate'
}

constellation = {
    'name': 'USS Constellation',
    'nation': 'United States',
    'level': 3,
    'type': 'frigate'
}


carrierNames = (kittyHawk, enterprise, nimitz, ford)

class Carrier:
    def __init__(self, name, country, level):
        self.name = name
        self.country = country
        self.level = level
        self.health = carriersType['size']
        self.cooldown = 2
        self.ready = True

        # Determines Runway Integrity, how much health the ship can drop to before it cannot launch fighters

        if level >= 1:
            self.runBreak = 2
        else:
            self.runBreak = 3

    # Ship status

    def __str__(self):
        return f'{self.country} Level {self.level} Aircraft Carrier: {self.name}'

    # Cooldown reduction as a turn passes

    def turn(self):
        # Reduces cooldown by 1
        self.cooldown -= 1

        # If cooldown has reached 0, enable the ship again
        if self.cooldown == 0:
            self.ready = True


    # When the ship is hit

    def damaged(self, split, collateralFactor, instaSinkPotential, gRC):

        # Calculates collateral damage, the higher the factor the less likely
        if randint(1, collateralFactor) == 1:
            collateral = 1
        else:
            collateral = 0

        # Calculates if damage is split
        if split:
            splitDamage = 0.5
        else:
            splitDamage = 0

        # Calculates if ship is InstaSunk
        if instaSinkPotential and randint(0, 100-carriersType['torp instaSink']) == 0:
            instaSink = True
        else:
            instaSink = False

        # Reduces health
        self.health -= 1 + collateral - splitDamage

        if instaSink or gRC:
            self.health = 0
        if self.health == 0:
            return 'Ship has sunk!'
        return 'Ship has taken a hit!'

    def runway_working(self):
        return self.health >= self.runBreak

    def attack(self, xCoord, yCoord):
        if self.runway_working() and self.ready:
            print(f'Fighters dispatched and initiating attack run at {xCoord}{yCoord}, stand by.')
            self.cooldown = 2
            self.ready = False
        elif not self.runway_working():
            print(f'Aircraft carrier runway is inoperational due to enemy fire.')
        elif not self.ready:
            print(f'Fighters are currently rearming and refueling. Please wait.')
        carrier.turn()


# Strings are placeholders

ships = (carriersType, 'battleshipsType', 'destroyersType', 'submarineType', 'frigateType')

# Localized test routine

carrier = Carrier(enterprise['name'], enterprise['nation'], enterprise['level'])
