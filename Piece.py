class Piece:

    def __init__(self, board, color, position):
        self.color = color
        self.type = type(self).__name__.lower()
        self.position = position
        self.board = board
