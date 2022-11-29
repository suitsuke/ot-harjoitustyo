
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
        self.testdb = sqlite3.connect("src/tests/userstickers.db")
        self.testdb.isolation_level = None
        self.testdb.execute(
            "CREATE TABLE UserStickers (user_id INTEGER REFERENCES Users, sticker_id INTEGER REFERENCES Stickers)")
        self.testdb.execute(
            "INSERT INTO UserStickers (user_id, sticker_id) VALUES (0, 0)")
        #self.testdb = testdb
        #self.repo = StickersRepository(self.testdb)
        self.service = StickerService()

    def test_total_stickers(self):
        self.assertEqual(self.service.total_stickers(), 11) #total amount of stickers in db
    
    def test_total_stickers_by_user(self):
        self.assertEqual(self.service.total_stickers_by_user(1), [])
        self.assertEqual(self.service.total_stickers_by_user(0), [0])
        self.assertEqual(self.service.total_stickers_by_user(2), [])

    
    def test_add_sticker(self):
        self.service.add_sticker(1) #add a random sticker to user 1, in this case nr 5
        self.assertEqual(len(self.service.total_stickers_by_user(0)), 1) #oletuksena tietokannassa
        self.assertEqual(len(self.service.total_stickers_by_user(2)), 0) #ei lisätty mitään
        self.assertEqual(len(self.service.total_stickers_by_user(1)), 1) #testattava

        #testaa vielä mitä tapahtuu kun kaikki mahdolliset tarrat on lisätty

        #self.assertEqual(self.service.add_sticker(1), 5) #test for randomness ok
        #self.assertEqual(len(self.service.total_stickers_by_user(1)), 1)
