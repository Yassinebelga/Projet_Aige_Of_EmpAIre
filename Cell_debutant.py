from vector import Vector

class Cell:

    def __init__ (self):
        self.v = Vector()
        self.e = Vector()
        self.occupied = False
        self.entity = None