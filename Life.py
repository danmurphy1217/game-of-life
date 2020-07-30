import random
from colorama import Fore, Back
import numpy as np

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
        [print(Fore.GREEN + Back.WHITE + "|" + Back.RESET + "".join([Fore.GREEN  + " " + "#" + " " if val == 1 else " . " for val in board[i]]) + Back.WHITE + " |" + Back.RESET) for i in range(len(board))]
        print(border)

    def nextBoardState(self, initialState):
        # Rule 1. Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
        # Rule 2. Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
        # Rule 3. Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
        # Rule 4. Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
        newState = GameOfLife.deadState(self)

        def liveNeighbors(board):
            height = self.height
            width = self.width
            for x in range(0, height):
                for y in range(0, width):
                    cell = board[x][y]
                    return cell
                    # if x==0 or y==0:
                    #     pass # edge case 1
                    # elif x==4 or y==4:
                    #     pass # edge case 2
                    # else:
                    #     alivesTotal = np.sum([board[x+1][y], board[x-1][y], board[x][y+1], board[x][y-1]])

                    #     return np.sum([board[x+1][y], board[x-1][y], board[x][y+1], board[x][y-1]])

        return liveNeighbors(newState)
if __name__ == "__main__":
    Game = GameOfLife(height = 5, width = 5)
    state = Game.randomState()
    # Game.prettyPrintBoard(state)
    print(Game.nextBoardState(state))
    
    