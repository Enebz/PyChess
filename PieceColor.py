
class PieceColor:

    def __init__(self, display_color):
        self.display_color = display_color
        

class Black(PieceColor):

    def __init__(self, display_color):
        PieceColor.__init__(self, display_color)

class White(PieceColor):

    def __init__(self, display_color):
        PieceColor.__init__(self, display_color)