#!/usr/bin/python3
""" Unittest for City class """

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city(self):
        model = City()
        self.assertTrue(type(model.name) is str)

if __name__ == "__main__":
    unittest.main()
