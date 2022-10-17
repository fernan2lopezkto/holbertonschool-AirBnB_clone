#!/usr/bin/python3
""" Unittest for Amenity class """

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity(self):
        model = Amenity()
        self.assertTrue(type(model.name) is str)

if __name__ == "__main__":
    unittest.main()
