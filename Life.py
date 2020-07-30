import random
from colorama import Fore, Back
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
    def randomState(self):
        height = self.height
        width = self.width
        board = [[random.randint(0, 1) for i in range(width)] for j in range(height)]
        def render(board):
            """Helper function to pretty print board."""
            border_width = len(board[0]) + 1
            border = Back.WHITE + Fore.GREEN + " - "*len(range(border_width)) + Back.RESET            
            print(border)
            [print(Fore.GREEN + Back.WHITE + "|" + Back.RESET + "".join([Fore.GREEN  + " " + "#" + " " if val == 1 else " . " for val in board[i]]) + Back.WHITE + " |" + Back.RESET) for i in range(len(board))]
            print(border)
            
        return render(board)    


if __name__ == "__main__":
    Game = GameOfLife(height = 30, width = 30)
    state = Game.randomState()
    
    