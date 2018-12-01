from collections import deque

class Explorer:
    def __init__(self, map):
        self.__map = map
        self.visited = set([])
        self.islands = 0
    
    def explore(self):
        for coordinate in self.__map:
            if coordinate in self.visited:
                continue
            
            if coordinate.land:
                self.islands += 1

            self.exploreCoordinate(coordinate)
        
        return self.islands

    def exploreCoordinate(self, start):
        toExplore = deque()
        toExplore.append(start)

        while True:
            try:
                coordinate = toExplore.popleft()

                if coordinate == None:
                    continue
                
                if coordinate in self.visited:
                    continue

                self.visited.add(coordinate)

                if(coordinate.land):
                    toExplore.append(self.__map.northOf(coordinate))
                    toExplore.append(self.__map.southOf(coordinate))
                    toExplore.append(self.__map.eastOf(coordinate))
                    toExplore.append(self.__map.westOf(coordinate))
            except IndexError:
                break