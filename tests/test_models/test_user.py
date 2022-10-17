#!/usr/bin/python3
"""unittest for user attributes"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_user(self):
        model = User()
        self.assertTrue(type(model.email) is str)
        self.assertTrue(type(model.password) is str)
        self.assertTrue(type(model.first_name) is str)
        self.assertTrue(type(model.last_name) is str)

if __name__ == "__main__":
    unittest.main()
