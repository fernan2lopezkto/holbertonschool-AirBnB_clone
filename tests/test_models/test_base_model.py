#!/usr/bin/python3
""" tests for base model """

import unittest
from models.base_model import BaseModel
import time


class Test_base_model(unittest.TestCase):
    """
    test base model
    """
    def setUp(self):
        """ set up a BaseModel instance """
        bm = BaseModel()

    def test_save(self):
        bm = BaseModel()
        time.sleep(1)
        bm.save()
        self.assertFalse(bm.created_at == bm.updated_at)

    def test_self_id(self):
        bm = BaseModel()
        self.assertEqual(type(bm.id), str)

    def test_created_at(self):
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "created_at"))

    def test_updated_at(self):
        bm = BaseModel()
        time.sleep(1)
        bm.save()
        self.assertTrue(hasattr(bm, "updated_at"))
        self.assertTrue(bm.created_at != bm.updated_at)

    def test___str__(self):
        bm = BaseModel()
        self.assertEqual(type(bm.__str__()), str)

    def test_to_dict(self):
        bm = BaseModel()
        self.assertEqual(type(bm.to_dict()), dict)

if __name__ == '__main__':
    unittest.main()