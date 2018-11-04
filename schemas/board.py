import numpy as np
import random

class Board:
    def __init__(self, size, board=None):
        self.size = size

        if board is None: 
            self.board = np.zeros(self.size * self.size, dtype=int).reshape(self.size, self.size)
        else:
            self.board = board

    def __str__(self):
        return(f"Size: {self.size}\n{self.board}")

    def board_to_number(self, player):
        """
        Converts a CodeNames board, with Red, Blue, Empty and Black cards to an integer, to a decimal number, for the specified player.
        Note that the perspective is that of the spymaster.
        The Board is treated as a multi-dimensional array of 0s and 1s.
        For the Red player, all the Red spots are treated as 1s and everything else as 0s, and vice versa for the Blue player.
        """
        print(f"Player: {player}")

        board_string = ""
        for row in self.board:
            for element in row:
                if element == player.value:
                    element_string = str(int(element))
                    board_string += element_string
                else:
                    board_string += '0'
        
        return int(board_string, 2)

    @classmethod 
    def number_to_board(cls, player, number, size):
        """
        Returns a board with the specified player's elements set to 1.
        """

        board = Board(size)
        i, j = size - 1, size - 1

        # Converts number to a string with binary representation
        # Strips the '0' and the 'b'
        board_string = bin(number)[2:]
        print(board_string)
        board_string = board_string[::-1]

        assert len(board_string) - 2 <= size * size 

        for element in board_string:
            board.set_element(i, j, int(element))
            if j == 0:
                j = size - 1
                i -= 1
            else:
                j -= 1

        return Board.get_flipped_board(board)
    
    def get_size(self):
        return self.size

    def get_element(self, i, j):
        return board[i][j]
    
    def set_element(self, i, j, element):
        # Since there are only 4 kinds of tiles
        self.board[i][j] = element % 4

    def get_board(self):
        """
        Gets the raw numpy.nd array from the Board object.
        """
        return self.board

    @classmethod 
    def generate_random_board(cls, size):
        board = Board(size)

        for i in range(size):
            for j in range(size):
                random_element = random.choice(range(4))
                board.set_element(i, j, random_element)

        return board

    @classmethod
    def get_flipped_board(cls, board):
        """
        Returns the board, from the opposite perspective.
        That is, given a board from the perspective of a spymaster,
        gets it from the perspective of the player, and vice versa.
        """
        size = board.get_size()
        grid = board.get_board()
        grid = np.rot90(grid)
        grid = np.rot90(grid)

        return Board(size, grid) 
