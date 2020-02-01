class Location(tuple):

    def __new__(cls, *args):
        return tuple.__new__(cls, args)

    def __reduce__(self):
        return (self.__class__, tuple(self))

    def __add__(self, other):
        return Location(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other):
        return Location(self[0] - other[0], self[1] - other[1])

# class Locator:

#     def __init__(self):


#     def GetSquare(self, loc):
#         cols = "abcdefgh"
#         rows = "12345678"
#         if len(loc) != 2:
#             return None
#         if loc[0].lower() not in cols:
#             return None
#         if loc[1].lower() not in rows:
#             return None
#         col = cols.index(loc[0])
#         row = rows.index(loc[1])
#         return (col, row)





