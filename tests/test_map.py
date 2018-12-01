import unittest
from islands.map import Map
from islands.coordinate import Coordinate

class TestMap(unittest.TestCase):
    def test_it_starts_from_a_base_of_0(self):
        matrix = [
            [1],
        ]
        map = Map(matrix)
        
        self.assertEqual(len(list(map)), len(matrix))
        self.assertEqual(list(map)[0].x, 0)
        self.assertEqual(list(map)[0].y, 0)
        self.assertEqual(list(map)[0].land, True)

    def test_it_iterates_a_multi_dimensional_array(self):
        matrix = [
            [1, 1, 1],
            [1, 1, 1],
        ]
        map = Map(matrix)
        
        self.assertEqual(len(list(map)), len(matrix) * len(matrix[0]))

class TestMapDirections(unittest.TestCase):
    def setUp(self):
        matrix = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]
        self.map = Map(matrix)
        self.start = Coordinate(1, 1, 0)        

    def test_north_of(self):
        end = self.map.northOf(self.start)
        self.assertEqual(end.x, self.start.x)
        self.assertEqual(end.y, self.start.y-1)

    def test_south_of(self):
        end = self.map.southOf(self.start)
        self.assertEqual(end.x, self.start.x)
        self.assertEqual(end.y, self.start.y+1)

    def test_east_of(self):
        end = self.map.eastOf(self.start)
        self.assertEqual(end.x, self.start.x-1)
        self.assertEqual(end.y, self.start.y)

    def test_west_of(self):
        end = self.map.westOf(self.start)
        self.assertEqual(end.x, self.start.x+1)
        self.assertEqual(end.y, self.start.y)