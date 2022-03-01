import unittest
from AreaOfCirlce import circle_area
from math import pi


#To unit test: python -m unittest test_circle
class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #Test area when radius is 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)
        