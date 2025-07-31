import random

blacklist = []

class Placer:
    def __init__(self, difficulty, size):

        self.difficulty = difficulty

        # The tendency number indicates the strength 1-10
        if difficulty == 0: # Civilian, always places everything in the middle next to each other
            centerTendency = 10
            edgeTendency = 1
            adjacentTendency = 10
        elif difficulty == 1: # Trainee, always places everything either in the middle or at the very edge, often with ships next to each other
            centerTendency = 10
            edgeTendency = 10
            adjacentTendency = 8
        elif difficulty == 2: # Seaman, places things more towards the edge but ships are still close together
            centerTendency = 1
            edgeTendency = 10
            adjacentTendency = 7
        elif difficulty >= 3 and difficulty <= 4: # Ensign & Commander, places things completely randomly
            centerTendency = 1
            edgeTendency = 1
            adjacentTendency = 1
        elif difficulty == 5: # Captain, avoids certain trends
            centerTendency = 1
            edgeTendency = 1
            adjacentTendency = 1
            # blacklist
        elif difficulty == 6: # Admiral, places strategically


        self.gridSize = size
        self.board = self.board = [[None for _ in range(size)] for _ in range(size)]

    def place(self, size)