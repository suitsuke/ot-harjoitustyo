
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
        self.testdb = sqlite3.connect("src/tests/userstickers.db")
        self.testdb.isolation_level = None
        self.testdb.execute(
            "CREATE TABLE UserStickers (user_id INTEGER REFERENCES Users, sticker_id INTEGER REFERENCES Stickers)")
        self.testdb.execute(
            "INSERT INTO UserStickers (user_id, sticker_id) VALUES (0, 0)")
        #self.testdb = testdb
        #self.repo = StickersRepository(self.testdb)
        self.service = StickerService()
        self.stickers_amount = 11
    
    def tearDown(self):
        os.remove("src/tests/userstickers.db")

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
        #self.assertEqual(self.service.add_sticker(1), (1,5)) #for testing
        #testaa vielä mitä tapahtuu kun kaikki mahdolliset tarrat on lisätty
        #self.assertEqual(len(self.service.total_stickers_by_user(1)), 1)

    def test_add_all_stickers(self):
        #self.service.add_sticker(3)
        #self.assertEqual(len(self.service.total_stickers_by_user(3)), 1)
        #self.service.add_sticker(3)
        #self.assertEqual(len(self.service.total_stickers_by_user(3)), 2)
        for i in range(1,self.stickers_amount+1):
            self.service.add_sticker(3)
            self.assertEqual(len(self.service.total_stickers_by_user(3)), i)
        over_added = self.service.add_sticker(3)
        self.assertEqual(len(self.service.total_stickers_by_user(3)), 11)    
        self.assertEqual(over_added, -1)
        
