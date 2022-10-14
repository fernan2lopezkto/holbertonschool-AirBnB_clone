#!/usr/bin/python3
""" tests for base model """

import unittest
from models import storage
from models.engine.file_storage import FileStorage

class Test_File_Storage(unittest.TestCase):
    """
    test base model
    """
    def test_1_(self):
        a = FileStorage()
        self.assertEqual(type(a), type(storage))
        self.assertTrue(isinstance(a, FileStorage))

if __name__ == '__main__':
    unittest.main()