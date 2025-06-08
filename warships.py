from random import *
from weapons import *

# Carriers

kittyHawk = {
    'name': 'USS Kitty Hawk',
    'nation': 'United States',
    'level': 0,
    'type': 'Carrier'
}

enterprise = {
    'name': 'USS Enterprise',
    'nation': 'United States',
    'level': 1,
    'type': 'Carrier'
}

nimitz = {
    'name': 'Nimitz',
    'nation': 'United States',
    'level': 2,
    'type': 'Carrier'
}

ford = {
    'name': 'Ford',
    'nation': 'United States',
    'level': 3,
    'type': 'Carrier'
}

carriers = {
    'name': 'Aircraft Carrier',
    'size': 5,
    'armament': 'fighter',
    'torp acc': 90,
    'torp instaSink': 5,
    'cooldown': 2,
    'runBreak': 3,
    'ships': [kittyHawk, enterprise, nimitz, ford]
}

# Battleships

washington = {
    'name': 'USS Washington',
    'nation': 'United States',
    'level': 0,
    'type': 'Battleship'
}

north_carolina = {
    'name': 'USS North Carolina',
    'nation': 'United States',
    'level': 1,
    'type': 'Battleship'
}

wisconson = {
    'name': 'USS Wisconsin',
    'nation': 'United States',
    'level': 2,
    'type': 'Battleship'
}

montana = {
    'name': 'USS Montana',
    'nation': 'United States',
    'level': 3,
    'type': 'Battleship'
}

battleships = {
    'name': 'Battleship',
    'size': 4,
    'armament': 'gun',
    'torp acc': 70,
    'torp instaSink': 15,
    'ships': [washington, north_carolina, wisconson, montana]
}

# Destroyers

decatur = {
    'name': 'USS Decatur',
    'nation': 'United States',
    'level': 0,
    'type': 'Destroyer'
}

fletcher = {
    'name': 'USS Fletcher',
    'nation': 'United States',
    'level': 1,
    'type': 'Destroyer'
}

spruance = {
    'name': 'USS Spruance',
    'nation': 'United States',
    'level': 2,
    'type': 'Destroyer'
}

intrepid = {
    'name': 'USS Intrepid',
    'nation': 'United States',
    'level': 3,
    'type': 'Destroyer'
}

destroyers = {
    'name': 'Destroyer',
    'size': 3,
    'armament': 'missile',
    'torp acc': 50,
    'torp instaSink': 55,
    'ships': [decatur, fletcher, spruance, intrepid]
}

# Submarines

nautilus = {
    'name': 'USS Nautilus',
    'nation': 'United States',
    'level': 0,
    'type': 'Submarine'
}

losAngeles = {
    'name': 'USS Los Angeles',
    'nation': 'United States',
    'level': 1,
    'type': 'Submarine'
}

seawolf = {
    'name': 'USS Seawolf',
    'nation': 'United States',
    'level': 2,
    'type': 'Submarine'
}

wahoo = {
    'name': 'USS Wahoo',
    'nation': 'United States',
    'level': 3,
    'type': 'Submarine'
}

submarines = {
    'name': 'Submarine',
    'size': 3,
    'armament': 'torpedo',
    'torp acc': 40,
    'torp instaSink': 75,
    'ships': [nautilus, losAngeles, seawolf, wahoo]
}

# Frigate names

knox = {
    'name': 'USS Knox',
    'nation': 'United States',
    'level': 0,
    'type': 'Frigate'
}

brooke = {
    'name': 'USS Brooke',
    'nation': 'United States',
    'level': 1,
    'type': 'Frigate'
}

independence = {
    'name': 'USS Independence',
    'nation': 'United States',
    'level': 2,
    'type': 'Frigate'
}

constellation = {
    'name': 'USS Constellation',
    'nation': 'United States',
    'level': 3,
    'type': 'Frigate'
}

frigates = {
    'name': 'Frigate',
    'size': 2,
    'armament': 'autocannon',
    'torp acc': 30,
    'torp instaSink': 75,
    'ships': [knox, brooke, independence, constellation]
}

class Ship:
    def __init__(self, shipType, level, country):

        # User parameter-dependent attributes
        self.country = country
        self.level = level

        # Ship class-dependent attributes
        self.type = shipType['name']
        self.health = shipType['size']
        # self.cooldown = shipType['cooldown']
        self.torpedoAcc = shipType['torp acc']
        self.torpedoInstaSink = shipType['torp instaSink']

        # Ship-dependent attributes
        self.name = shipType['ships'][level]['name']

        # Fixed attributes
        self.ready = True

        # Unique Standard attributes

        # Runway integrity for carriers, normally 3 unless level 1+, then 4
        if shipType == carriers:
            self.runBreak = shipType['runBreak']
            if self.level > 0:
                self.runBreak += 1

        # Armor for battleships, 30% if level 1+, otherwise 0
        self.armor = 0
        if self.level > 0:
            self.armor += 30

        # Active defense for destroyers, 30% if level 1+, otherwise 0
        self.activeDefense = 0
        if self.level > 0:
            self.activeDefense += 30
        self.activeDefenseRange = 1

        # Stealth for submarines, 30% if level 1+, 50% if level 2+, otherwise 0
        self.stealth = 0
        if self.level > 0:
            self.stealth += 30
        elif self.level > 1:
            self.stealth += 50

        # Evasion for frigates, 30% if level 1+, otherwise 0
        self.evasion = 0
        if self.level > 0:
            self.evasion += 30

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
        if instaSinkPotential and randint(0, 100 - carriers['torp instaSink']) == 0:
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

ships = (carriers, battleships, destroyers, submarines, frigates)

# Levels unlocked by user (placeholder)
caLevel = 0
baLevel = 0
deLevel = 0
suLevel = 0
frLevel = 0

# Country used by player (placeholder)
country = 'United States'


# Localized test routine

carrier = Ship(carriers, caLevel, country)
battleship = Ship(battleships, baLevel, country)
destroyer = Ship(destroyers, deLevel, country)
submarine = Ship(submarines, suLevel, country)
frigate = Ship(frigates, frLevel, country)
