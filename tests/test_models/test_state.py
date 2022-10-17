#!/usr/bin/python3
""" Unittest for State class """

import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_state(self):
        model = State()
        self.assertTrue(type(model.name) is str)

if __name__ == "__main__":
    unittest.main()
