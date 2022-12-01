
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
        # total amount of stickers in db
        self.assertEqual(self.service.total_stickers(), 11)

    def test_total_stickers_by_user(self):
        self.assertEqual(self.service.total_stickers_by_user(1), [])
        self.assertEqual(self.service.total_stickers_by_user(0), [0])
        self.assertEqual(self.service.total_stickers_by_user(2), [])

    def test_add_sticker(self):
        # add a random sticker to user 1, in this case nr 5
        self.service.add_sticker(1)
        # oletuksena tietokannassa
        self.assertEqual(len(self.service.total_stickers_by_user(0)), 1)
        # ei lisätty mitään
        self.assertEqual(len(self.service.total_stickers_by_user(2)), 0)
        self.assertEqual(
            len(self.service.total_stickers_by_user(1)), 1)  # testattava

        # self.assertEqual(self.service.add_sticker(1), (1,5)) #for testing

    def test_add_all_stickers(self):
        # add stickers full for a user, check that they are added and finally return -1
        for i in range(1, self.stickers_amount+1):
            self.service.add_sticker(3)
            self.assertEqual(len(self.service.total_stickers_by_user(3)), i)
        over_added = self.service.add_sticker(3)
        self.assertEqual(len(self.service.total_stickers_by_user(3)), 11)
        self.assertEqual(over_added, -1)
        over_added = self.service.add_sticker(3)
        self.assertEqual(over_added, -1)
    
    def test_remove_sticker(self):
        for i in range(1, self.stickers_amount+1):
            self.service.add_sticker(3)
            self.assertEqual(len(self.service.total_stickers_by_user(3)), i)
        self.assertEqual(self.service.total_stickers_by_user(3), [1,2,3,4,5,6,7,8,9,10,11])
        
        self.service.remove_sticker(3,1)
        self.assertEqual(self.service.total_stickers_by_user(3), [2,3,4,5,6,7,8,9,10,11])

        self.service.remove_sticker(3,10)
        self.assertEqual(self.service.total_stickers_by_user(3), [2,3,4,5,6,7,8,9,11])

        self.service.remove_sticker(3,10)
        self.assertEqual(self.service.total_stickers_by_user(3), [2,3,4,5,6,7,8,9,11])
