from Board import Board

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

bR = {"data":{"color":"black", "type":"rook", "board_icon":"R"}}
bQ = {"data":{"color":"black", "type":"queen", "board_icon":"Q"}}
bK = {"data":{"color":"black", "type":"king", "board_icon":"K"}}
bP = {"data":{"color":"black", "type":"pawn", "board_icon":"P"}}
bN = {"data":{"color":"black", "type":"knight", "board_icon":"N"}}
bB = {"data":{"color":"black", "type":"bishop", "board_icon":"B"}}

wR = {"data":{"color":"white", "type":"rook", "board_icon":"R"}}
wQ = {"data":{"color":"white", "type":"queen", "board_icon":"Q"}}
wK = {"data":{"color":"white", "type":"king", "board_icon":"K"}}
wP = {"data":{"color":"white", "type":"pawn", "board_icon":"P"}}
wN = {"data":{"color":"white", "type":"knight", "board_icon":"N"}}
wB = {"data":{"color":"white", "type":"bishop", "board_icon":"B"}}

nE = {"data":{"color":"none", "type":"empty", "board_icon":"+"}}

# chess_board = [
#     #"a" "b" "c" "d" "e" "f" "g" "h"
#     [wR, wN, wB, wQ, wK, wB, wN, wR],
#     [wP, wP, wP, wP, wP, wP, wP, wP],
#     [nE, nE, nE, nE, nE, nE, nE, nE],
#     [nE, nE, nE, nE, nE, nE, nE, nE],
#     [nE, nE, nE, nE, nE, nE, nE, nE],
#     [nE, nE, nE, nE, nE, nE, nE, nE],
#     [bP, bP, bP, bP, bP, bP, bP, bP],
#     [bR, bN, bB, bQ, bK, bB, bN, bR],
# ]

# def PrintBoard(board, flip = False):
#     board = board if flip else FlipBoard(board)
#     board_p = ""
#     for row in board:
#         for piece in row:
#             color = bcolors.FAIL if piece["data"]["color"] == "black" else bcolors.OKGREEN if piece["data"]["color"] == "white" else bcolors.ENDC
#             board_p += f"{color}{piece['data']['board_icon']}{bcolors.ENDC}   "
#         board_p+="\n\n"
#     print(board_p)

# def FlipBoard(board):
#     rev_board = list(reversed(board))
#     new_board = []
#     for row in rev_board:
#         new_board.append(list(reversed(row)))
#     return new_board


chess_board = Board(
    [
    #"a" "b" "c" "d" "e" "f" "g" "h"
    [wR, wN, wB, wQ, wK, wB, wN, wR],
    [wP, wP, wP, wP, wP, wP, wP, wP],
    [nE, nE, nE, nE, nE, nE, nE, nE],
    [nE, nE, nE, nE, nE, nE, nE, nE],
    [nE, nE, nE, nE, nE, nE, nE, nE],
    [nE, nE, nE, nE, nE, nE, nE, nE],
    [bP, bP, bP, bP, bP, bP, bP, bP],
    [bR, bN, bB, bQ, bK, bB, bN, bR],
    ]
)



def GetPiece(board, square):
    return board[square[1]][square[0]]

chess_board.PrintBoard()





