from tkinter import *
from PIL import ImageTk, Image

import warships
import shop
import grid

ownedShips = []

# This is the number for each ship's level (shopShip); goes from carrier to frigate (destroyer before submarine).
# It starts as none but will be replaced from reading a txt file
equippedShips = [None, None, None, None, None]

class Drydock:
    def __init__(self, root, country, colors):
        pass