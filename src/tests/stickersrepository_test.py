import unittest
import sqlite3
import os
from repositories.stickers_repository import StickersRepository

class TestStickersRepository(unittest.TestCase):
    def setUp(self):
        os.remove("test_userstickers.db")
        db = sqlite3.connect("src/tests/test_userstickers.db")
        db.isolation_level = None
        db.execute("CREATE TABLE UserStickers (user_id INTEGER REFERENCES Users, sticker_id INTEGER REFERENCES Stickers)")
        self.db = StickersRepository("test_userstickers.db")


    def test_add_sticker(self):
        self.assertEqual(0,0)   #test for tests
        self.db
        #i=self.db.add_sticker(2,3)
        self.assertEqual(i, (2,3))
