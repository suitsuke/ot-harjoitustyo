
import unittest
import sqlite3
import os
from repositories.stickers_repository import StickersRepository
from services.stickerservice import StickerService

default_stickerdb = "data/stickers.db"
default_userdb = "tests/userstickers.db"


class TestStickersRepository(unittest.TestCase):
    def setUp(self):
        # set up userstickers
        os.remove("src/tests/userstickers.db")
        testdb = sqlite3.connect("src/tests/userstickers.db")
        testdb.isolation_level = None
        testdb.execute("CREATE TABLE UserStickers (user_id INTEGER REFERENCES Users, sticker_id INTEGER REFERENCES Stickers)")
        #testdb.execute("CREATE TABLE UserStickers (user_id, sticker_id)")
        testdb.execute(
            "INSERT INTO UserStickers (user_id, sticker_id) VALUES (0, 0)")
        self.testdb = testdb
        self.repo = StickersRepository(self.testdb)
        self.service = StickerService()

    def test_total_stickers(self):
        self.assertEqual(self.service.total_stickers(), 11) #total amount of stickers in db
    
    def test_total_stickers_by_user(self):
        self.assertEqual(self.service.total_stickers_by_user(1), 0)
    
    #def test_add_sticker(self):
    #    self.service.add_sticker(1)
        #self.assertEqual(, )
