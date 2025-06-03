from random import *
from weapons import *

# All types of ships

carriersType = {
    'name': 'Aircraft Carriers',
    'size': 5,
    'armament': 'fighters',
    'torp acc': 90,
    'torp instaSink': 5
}

# Ship names

kittyHawk = {
    'name': 'USS Kitty Hawk',
    'nation': 'United States',
    'level': 0
}

enterprise = {
    'name': 'USS Enterprise',
    'nation': 'United States',
    'level': 1
}

nimitz = {
    'name': 'Nimitz',
    'nation': 'United States',
    'level': 2
}

ford = {
    'name': 'Ford',
    'nation': 'United States',
    'level': 3
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


# Localized test routine

carrier = Carrier(enterprise['name'], enterprise['nation'], enterprise['level'])

while True:
    carrier.turn()
    carrier.attack()