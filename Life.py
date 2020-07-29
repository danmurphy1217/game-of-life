import random

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
        return board
        def render(board, height, width):
            """Helper function to pretty print board."""
            pass


if __name__ == "__main__":
    Game = GameOfLife(height = 10, width = 5)
    print(Game.randomState())
    
    