import unittest
from islands.coordinate import Coordinate

class TestCoordinate(unittest.TestCase):
    def test_land(self):
        self.assertEqual(Coordinate(0, 0, 0).land, False)
        self.assertEqual(Coordinate(0, 0, 1).land, True)