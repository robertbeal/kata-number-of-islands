import unittest
from islands.map import Map
from islands.explorer import Explorer

class TestMap(unittest.TestCase):
    def test_exploring_square_maps(self):
        matrix = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 1, 1],
        ]
        map = Map(matrix)
        explorer = Explorer(map)
        
        self.assertEqual(explorer.explore(), 3)

    def test_exploring_non_square_maps(self):
        matrix = [
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
        ]
        map = Map(matrix)
        explorer = Explorer(map)
        
        self.assertEqual(explorer.explore(), 4)