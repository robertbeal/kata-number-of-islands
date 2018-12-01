from islands.coordinate import Coordinate

class Map:
    def __init__(self, matrix):
        self.__matrix = matrix

    def __iter__(self):
        for x in range(len(self.__matrix)):
            for y in range(len(self.__matrix[x])):
                yield self.__coordinateFor(x, y)
    
    def northOf(self, coordinate):
        return self.__coordinateFor(coordinate.x, coordinate.y-1)

    def southOf(self, coordinate):
        return self.__coordinateFor(coordinate.x, coordinate.y+1)

    def eastOf(self, coordinate):
        return self.__coordinateFor(coordinate.x-1, coordinate.y)

    def westOf(self, coordinate):
        return self.__coordinateFor(coordinate.x+1, coordinate.y)

    def __coordinateFor(self, x, y):
        if x < 0 or x >= len(self.__matrix):
            return None
        if y < 0 or y >= len(self.__matrix[0]):
            return None

        return Coordinate(x, y, self.__matrix[x][y])
