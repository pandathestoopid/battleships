import random

blacklist = []
orientations = ['horizontal', 'vertical']

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
            centerTendency = 1
            edgeTendency = 1
            adjacentTendency = 1
            # baller

        self.gridSize = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    # Resets the board
    def reset(self):
        self.board = [[None for _ in range(self.gridSize)] for _ in range(self.gridSize)]

    # Places the ship
    def place(self, size):

        while True:

            orient = random.choice(orientations) # Picks an orientation for the ship
            if orient == 'horizontal':
                xReduce = 1
                yReduce = 0
            elif orient == 'vertical':
                xReduce = 0
                yReduce = 1

            # Chooses a spot to put the ship within the grid
            x = random.randint(0, self.gridSize - 1 - (size * xReduce))
            y = random.randint(0, self.gridSize - 1 - (size * yReduce))

            bad = False
            if orient == 'horizontal':
                for s in range(-1, size+1):
                    if self.board[y][x+s] is not None: # Checks main horizontal line
                        bad = True
                        print('oops')
                        break # Exits the for loop so that the continue statement skips the while loop
                    if y-1 >= 0 and self.board[y-1][x+s] is not None: # Checks above horizontal line (if it exists)
                        bad = True
                        print('oops')
                        break
                    if y+1 < self.gridSize and self.board[y+1][x+s] is not None: # Checks below horizontal line (if it exists)
                        bad = True
                        print('oops')
                        break
                if bad:
                    continue
                else:
                    for s in range(size):
                        self.board[y][x+s] = size # Updates the board if the checks pass
            elif orient == 'vertical':
                for s in range(-1, size+1):
                    if self.board[y+s][x] is not None: # Checks main vertical line
                        bad = True
                        print('oops')
                        break # Exits the for loop so that the continue statement skips the while loop
                    if x-1 >= 0 and self.board[y+s][x-1] is not None:  # Checks the left vertical line
                        bad = True
                        print('oops')
                        break
                    if x+1 < self.gridSize and self.board[y+s][x+1] is not None:  # Checks the right vertical line
                        bad = True
                        print('oops')
                        break
                if bad:
                    continue
                else:
                    for s in range(size):
                        self.board[y+s][x] = size # Updates the board if the checks pass

            print(x, y, orient, size)
            return x, y, orient # Returns the ship's origin placement coordinates to the grid
