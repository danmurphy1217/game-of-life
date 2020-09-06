import random
from colorama import Fore, Back
import numpy as np
import time

LIVE = 1
DEAD = 0

class GameOfLife:
    def __init__(self, height, width):
        """
        Parameters
        ----------
        height : (int)
            the height of the board
        width : (int)
            the width of the board
        """
        self.height = height 
        self.width = width
    def deadState(self):
        height = self.height
        width = self.width 
        board = [[0 for i in range(width)] for j in range(height)]
        return board
    def randomState(self):
        height = self.height
        width = self.width
        seed = random.seed(42)
        board = [[random.randint(0, 1) for i in range(width)] for j in range(height)]
        return board

    def prettyPrintBoard(self, board):
        """Helper function to pretty print board."""
        borderWidth = len(board[0]) + 1
        border = Back.WHITE + Fore.GREEN + " - "*len(range(borderWidth)) + Back.RESET            
        print(border)
        [print(Fore.GREEN + Back.WHITE + "|" + Back.RESET + "".join([Fore.GREEN  + " " + u"\u2588" + " " if val == 1 else " . " for val in board[i]]) + Back.WHITE + " |" + Back.RESET) for i in range(len(board))]
        print(border)

    def nextBoardState(self, initialState):
        # Rule 1. Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
        # Rule 2. Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
        # Rule 3. Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
        # Rule 4. Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
        newState = GameOfLife.deadState(self)
        width = self.width
        height = self.height
        
        def nextCellValue(coordinates, currentState):
            """
            Helper function to define the next value of the cell.
            
            Parameters
            ----------
            coordinates: (tuple)
                a tuple of the X and Y coordinates for the current cell.
            currentState: (matrix)
                the current board state.

            Returns
            ----------
            The new state of the cell (alive or dead).
            """
            x = coordinates[0] # X-coord is the first item in the tuple
            y = coordinates[1] # Y-coord is the second item in the tuple
            live_neighbors = 0
            for x1 in range((x-1), (x+1)+1):
                
                # If x coordinate is less than 0 or greater than/equal to the width, skip
                if x1<0 or x1 >= width:
                    continue
                for y1 in range((y-1), (y+1)+1):
                    # If y coordinate is less than 0 or greater than/equal to the height, skip
                    if y1<0 or y1>= height:
                        continue
                    # Skip calculation for current cell
                    if x1 == x and y1 == y:
                        continue
                    # Increment live_neighbors
                    if currentState[x1][y1] == LIVE:
                        live_neighbors += 1
            # GAME OF LIFE LOGIC
            if state[x][y] == LIVE:
                # if LIVE and has less than or 1 live neighbor, return DEAD
                if live_neighbors <= 1:
                    return DEAD
                # if LIVE and has less than or equal to 3 live neighbors, return LIVE
                elif live_neighbors <= 3:
                    return LIVE
                # otherwise, DEAD
                else:                    
                    return DEAD
            else:
                # if DEAD and has 3 live neighbors exactly, return LIVE
                if live_neighbors == 3:
                    return LIVE
                # otherwise, DEAD
                else:
                    return DEAD

        for x in range(0, height):
            for y in range(0, width):                
                newState[x][y] =  nextCellValue((x, y), initialState)
        return newState

    def runForever(self, initialState):
        """
        Run the game until the user exits.
        
        Parameters
        ----------
        initialState: (matrix)
            the intial state of the game.

        Returns
        ----------
        None
        """
        # initially, nextState == initialState
        nextState = initialState
        while True:
            # print initial state to console
            GameOfLife.prettyPrintBoard(self, nextState)
            # on each iteration, nextState is updated to equal the "nextBoardState"
            nextState = Game.nextBoardState(nextState)
            time.sleep(.05)


if __name__ == "__main__":
    Game = GameOfLife(height = 15, width = 15)
    state = Game.randomState()
    Game.runForever(state)
    
    