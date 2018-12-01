class Coordinate:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.land = value == 1

    def __eq__(self, other):
        if other == None:
            return False
            
        return (self.x == other.x) and (self.y == other.y)
    
    def __hash__(self):
        return hash(str(self.x) + "," + str(self.y))