import unittest
from stickersrepository_test import StickersRepository

class TestStickersRepository(unittest.TestCase):
    def setUp(self):
        self.db = StickersRepository("userstickers.db")

    def test_add_sticker(self):
        self.assertEqual(0,0)   #test for tests
        self.assertEqual(self.db.add_sticker(2,3), (2,3))
