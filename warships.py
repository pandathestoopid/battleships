from random import *

import shop
import grid

countries = ['United States', 'Soviet Union', 'United Kingdom', 'Germany', 'Japan']

countryColors = {
    'United States': '#0a3e8a',
    'Soviet Union': '#d93604',
    'United Kingdom': '#03194a',
    'Germany': '#ad8603',
    'Japan': '#bb0045'
}

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

lincoln = {
    'name': 'USS Abraham Lincoln',
    'nation': 'United States',
    'level': 2,
    'type': 'Carrier'
}

ford = {
    'name': 'USS Gerald R. Ford',
    'nation': 'United States',
    'level': 3,
    'type': 'Carrier'
}

# List of each nation's carriers
usCars = [kittyHawk, enterprise, lincoln, ford]
sovCars = None

carriers = {
    'name': 'Aircraft Carrier',
    'size': 5,
    'mArmament': 'Strike aircraft',
    'mArmDesc': 'A fleet of multi-role strike aircraft which can deliver shells, bombs, and torpedoes to enemy vessels. '
                'Takes one turn to cool down between sorties. Massive damage potential, but low accuracy. Vulnerable to being shot down.',
    'aaArmament': 'Fighter aircraft',
    'aaArmDesc': 'A fleet of air-superiority aircraft which can fire air-to-air missiles at enemy aircraft.'
                 'Three groups cycle to keep defenses always active, making the carrier almost invincible to air attacks.',
    'torp acc': 90,
    'torp instaSink': 5,
    'cooldown': 2,
    'runBreak': 3,
    'ships': [usCars, sovCars]
}

# Battleships

washington = {
    'name': 'USS Washington',
    'nation': 'United States',
    'level': 0,
    'type': 'Battleship'
}

northCarolina = {
    'name': 'USS Alabama',
    'nation': 'United States',
    'level': 1,
    'type': 'Battleship'
}

wisconsin = {
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

# List of each nation's battleships
usBats = [washington, northCarolina, wisconsin, montana]
sovBats = None

battleships = {
    'name': 'Battleship',
    'size': 4,
    'mArmament': '18-inch gun',
    'mArmDesc': 'An array of 18-inch guns, with consistent damage output and decent accuracy. Can get significant upgrades.',
    'aaArmament': 'AAA',
    'aaArmDesc': 'An array of anti-aircraft artillery (Triple-A) consisting of heavy cannons with proximity-fuse high explosive shells and machine guns.',
    'torp acc': 70,
    'torp instaSink': 15,
    'cooldown': 1,
    'ships': [usBats, sovBats]
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

usDests = [decatur, fletcher, spruance, intrepid]
sovDests = None

destroyers = {
    'name': 'Destroyer',
    'size': 3,
    'mArmament': 'missile',
    'mArmDesc': 'A guided air-based warhead which has high damage and accuracy, but high cooldown. '
                'Can be intercepted by some ships, and reveals nearby scout drones. '
                'Can eject the aerodynamic cap to reveal a sharp nose that can pierce water to hit submarines.',
    'aaArmament': 'RIM SAM',
    'aaArmDesc': 'Multiple pods of RIM surface-to-air missiles, guided by the ship\'s onboard radar.'
                 'Very high accuracy, but vulnerable to swarm attacks.',
    'torp acc': 50,
    'torp instaSink': 55,
    'cooldown': 3,
    'ships': [usDests, sovDests]
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

# List of each nations's subs
usSubs = [nautilus, losAngeles, seawolf, wahoo]
sovSubs = None

submarines = {
    'name': 'Submarine',
    'size': 3,
    'mArmament': 'torpedo',
    'mArmDesc': 'A large, guided warhead that travels under the ocean to a target. '
                'Higher damage potential and lower accuracy the smaller the target ship. '
                'Reloads for 5 turns after firing twice.',
    'aaArmament': 'VLS SSAM',
    'aaArmDesc': 'A group of sub-surface-to-air missiles stored in the submarine\'s vertical launch system. Fires at incoming aircraft.'
                 'Has significantly less accuracy than standard SAMs, so placing the sub near other air defense would be beneficial.',
    'torp acc': 40,
    'torp instaSink': 75,
    'cooldown': 6,
    'shots': 2,
    'ships': [usSubs, sovSubs]
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

# List of each nation's frigates
usFrigs = [knox, brooke, independence, constellation]
sovFrigs = None

frigates = {
    'name': 'Frigate',
    'size': 2,
    'mArmament': '120mm autocannon',
    'mArmDesc': 'An improved version of the BOFORS L/50 automatic gun, firing 120mm APFSDS shells at 80 RPM. '
                'Fires in bursts of five for each turn. Has a chance to spread its 1 damage over two squares. '
                'Chance to overheat after 3 consecutive fires, extreme chance after 4 fires.',
    'aaArmament': 'AA autocannon',
    'aaArmDesc': 'A gatling-style autocannon that fires 20mm explosive redbull cans at 6,000 RPM towards incoming aircraft.'
                 'Two are mounted on the ship which cycle to prevent overheating.',
    'torp acc': 30,
    'torp instaSink': 75,
    'cooldown': 5,
    'shots': 3,
    'ships': [usFrigs, sovFrigs]
}

class Ship:
    def __init__(self, shipType, level, country):

        # User parameter-dependent attributes
        self.country = country
        self.level = level

        # Ship type-dependent attributes
        self.type = shipType['name']
        self.health = shipType['size']
        self.shots = 1 # By default, the number of consecutive shots before cooldown is 1, but for frigates and submarines it can be higher.
        if shipType == submarines or shipType == frigates:
            self.shots = shipType['shots']
        self.armament = shipType['mArmament']
        self.cooldown = shipType['cooldown']
        self.torpedoAcc = shipType['torp acc']
        self.torpedoInstaSink = shipType['torp instaSink']

        # Ship-dependent attributes
        self.name = shipType['ships'][countries.index(self.country)][level]

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

# Upgrade config used by player (placeholder)



# Localized test routine

carrier = Ship(carriers, caLevel, country)
battleship = Ship(battleships, baLevel, country)
destroyer = Ship(destroyers, deLevel, country)
submarine = Ship(submarines, suLevel, country)
frigate = Ship(frigates, frLevel, country)
