from Color import Colored, ColorPrint
from Locator import Location as L
from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from PieceColor import Black, White, PieceColor


WHITE = False
BLACK = True

class Board:
    _Flipped = WHITE
    def __init__(self, pieces):
        self.pieces = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]

        self.pieces = [
            [
                Rook   (self, White, L(0,7)),
                Knight (self, White, L(0,6)),
                Bishop (self, White, L(0,5)),
                King   (self, White, L(0,4)),
                Queen  (self, White, L(0,3)),
                Bishop (self, White, L(0,2)),
                Knight (self, White, L(0,1)),
                Rook   (self, White, L(0,0)),
            ],
            [ Pawn(self, White, L(1,x)) for x in range(7,0,-1) ], 
            [], 
            [], 
            [], 
            [], 
            [ Pawn(self, Black, L(6,x)) for x in range(7,0,-1) ], 
            [
                Rook   (self, Black, L(7,7)),
                Knight (self, Black, L(7,6)),
                Bishop (self, Black, L(7,5)),
                King   (self, Black, L(7,4)),
                Queen  (self, Black, L(7,3)),
                Bishop (self, Black, L(7,2)),
                Knight (self, Black, L(7,1)),
                Rook   (self, Black, L(7,0)),
            ], 
        ]

    def PrintBoard(self, flip = False):
        board = self.FlipBoard(flip)
        board_p = ""
        for row in board:
            for piece in row:
                color = "red" if piece["data"]["color"] == "black" else "green" if piece["data"]["color"] == "white" else None
                board_p += Colored(f"{piece['data']['board_icon']}   ", color=color)      
            board_p+="\n\n"
        print(board_p)


    def FlipBoard(self, flip):
        self._Flipped = WHITE if self._Flipped == BLACK else BLACK
        process_board = list(reversed(self.pieces)) if not flip else self.pieces
        new_board = []
        for row in process_board:
            new_board.append(list(row) if not flip else list(reversed(row)))
        return new_board

    @property
    def Flipped(self):
        return self._Flipped


    