import unittest
import sqlite3
import os
from repositories.stickers_repository import StickersRepository


class TestStickersRepository(unittest.TestCase):
    def setUp(self):
        os.remove("src/tests/userstickers.db")
        testdb = sqlite3.connect("src/tests/userstickers.db")
        testdb.isolation_level = None
        #testdb.execute("CREATE TABLE UserStickers (user_id INTEGER REFERENCES Users, sticker_id INTEGER REFERENCES Stickers)")
        testdb.execute("CREATE TABLE UserStickers (user_id, sticker_id)")
        testdb.execute(
            "INSERT INTO UserStickers (user_id, sticker_id) VALUES (0, 0)")
        self.testdb = testdb
        self.repo = StickersRepository(self.testdb)

    def test_testinit(self):
        zero = self.testdb.execute("SELECT * FROM UserStickers").fetchone()
        self.assertEqual(zero, (0, 0))

    def test_add_sticker(self):
        # self.assertEqual(0,0)   #test for tests
        # self.db
        self.assertEqual(self.repo.add_sticker(2, 3), (2, 3))
        self.assertEqual(self.repo.add_sticker(1, 1), (1, 1))

    def test_remove_sticker(self):
        self.repo.add_sticker(1, 1)
        self.repo.add_sticker(2, 3)
        return
        # returns true if sticker was removed
        self.assertEqual(self.repo.remove_sticker(2, 3), True)
        # returns false if nothing was removed
        self.assertEqual(self.repo.remove_sticker(2, 5), False)
