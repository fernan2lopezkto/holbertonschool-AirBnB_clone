#!/usr/bin/python3
""" Unittest for Place class """

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_place(self):
        model = Place()
        self.assertTrue(type(model.name) is str)

if __name__ == "__main__":
    unittest.main()
