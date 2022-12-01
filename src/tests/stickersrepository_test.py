import unittest
import sqlite3
import os
from repositories.stickers_repository import StickersRepository
from services.stickerservice import StickerService


class TestStickersRepository(unittest.TestCase):
    def setUp(self):
        testdb = sqlite3.connect("src/tests/userstickers.db")
        testdb.isolation_level = None
        testdb.execute(
            "CREATE TABLE UserStickers (user_id INTEGER REFERENCES Users, sticker_id INTEGER REFERENCES Stickers)")
        #testdb.execute("CREATE TABLE UserStickers (user_id, sticker_id)")
        testdb.execute(
            "INSERT INTO UserStickers (user_id, sticker_id) VALUES (0, 0)")
        self.testdb = testdb
        self.repo = StickersRepository(self.testdb)

    def tearDown(self):
        os.remove("src/tests/userstickers.db")

    def test_testinit(self):
        zero = self.testdb.execute("SELECT * FROM UserStickers").fetchone()
        self.assertEqual(zero, (0, 0))

    def test_add_sticker(self):
        self.assertEqual(self.repo.add_sticker(2, 3), (2, 3))
        self.assertEqual(self.repo.add_sticker(1, 1), (1, 1))
        self.assertEqual(self.repo.add_sticker(3, 5), (3, 5))

    def test_remove_sticker(self):
        self.repo.add_sticker(1, 1)
        self.repo.add_sticker(2, 3)
        self.assertEqual(self.repo.find_all_by_user(0), [0])
        self.assertEqual(self.repo.find_all_by_user(1), [1])
        self.assertEqual(self.repo.find_all_by_user(2), [3])

        self.repo.remove_sticker(1,1)
        self.assertEqual(self.repo.find_all_by_user(0), [0])
        self.assertEqual(self.repo.find_all_by_user(1), [])
        self.assertEqual(self.repo.find_all_by_user(2), [3])

        self.repo.remove_sticker(1,1) #remove something that isnt in the db
        self.assertEqual(self.repo.find_all_by_user(0), [0])
        self.assertEqual(self.repo.find_all_by_user(1), [])
        self.assertEqual(self.repo.find_all_by_user(2), [3])

        self.repo.remove_sticker(2,3) #remove something that isnt in the db
        self.assertEqual(self.repo.find_all_by_user(0), [0])
        self.assertEqual(self.repo.find_all_by_user(1), [])
        self.assertEqual(self.repo.find_all_by_user(2), [])
        
        # returns true if sticker was removed
        #self.assertEqual(self.repo.remove_sticker(2, 3), True)
        # returns false if nothing was removed
        #self.assertEqual(self.repo.remove_sticker(2, 5), False)

    def test_find_all_by_user(self):
        self.repo.add_sticker(2, 3)
        self.repo.add_sticker(1, 1)
        self.repo.add_sticker(1, 5)
        self.repo.add_sticker(1, 6)
        self.repo.add_sticker(2, 1)
        self.assertEqual(self.repo.find_all_by_user(1), [1, 5, 6])
        self.assertEqual(self.repo.find_all_by_user(2), [1, 3])
