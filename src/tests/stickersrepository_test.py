import unittest
import sqlite3
import os
from repositories.stickers_repository import StickersRepository
from services.stickerservice import StickerService


class TestStickersRepository(unittest.TestCase):
    def setUp(self):
        os.remove("data/userstickers.db")
        testdb = sqlite3.connect("data/userstickers.db")
        testdb.isolation_level = None
        testdb.execute(
            "CREATE TABLE UserStickers (user_id INTEGER REFERENCES Users, sticker_id INTEGER REFERENCES Stickers)")
        testdb.execute(
            "INSERT INTO UserStickers (user_id, sticker_id) VALUES (0, 0)")
        testdb.execute(
            "CREATE TABLE Users (user_id INTEGER, name TEXT, action1 TEXT, action2 TEXT, action3 TEXT)")
        testdb.execute(
            "INSERT INTO Users (user_id, name, action1, action2, action3) VALUES (1, 'user1', 'action1', 'action2', 'action3')")
        testdb.execute(
            "INSERT INTO Users (user_id, name, action1, action2, action3) VALUES (2, 'user2', 'action1', 'action2', 'action3')")
        testdb.execute(
            "INSERT INTO Users (user_id, name, action1, action2, action3) VALUES (3, 'user3', 'action1', 'action2', 'action3')")
        self.testdb = testdb
        self.repo = StickersRepository(self.testdb)

    def tearDown(self):
        os.remove("data/userstickers.db")
        testdb = sqlite3.connect("data/userstickers.db")
        testdb.isolation_level = None
        testdb.execute(
            "CREATE TABLE UserStickers (user_id INTEGER REFERENCES Users, sticker_id INTEGER REFERENCES Stickers)")
        testdb.execute(
            "INSERT INTO UserStickers (user_id, sticker_id) VALUES (0, 0)")
        testdb.execute(
            "CREATE TABLE Users (user_id INTEGER, name TEXT, action1 TEXT, action2 TEXT, action3 TEXT)")
        testdb.execute(
            "INSERT INTO Users (user_id, name, action1, action2, action3) VALUES (1, 'user1', 'action1', 'action2', 'action3')")
        testdb.execute(
            "INSERT INTO Users (user_id, name, action1, action2, action3) VALUES (2, 'user2', 'action1', 'action2', 'action3')")
        testdb.execute(
            "INSERT INTO Users (user_id, name, action1, action2, action3) VALUES (3, 'user3', 'action1', 'action2', 'action3')")

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

        self.repo.remove_sticker(1, 1)
        self.assertEqual(self.repo.find_all_by_user(0), [0])
        self.assertEqual(self.repo.find_all_by_user(1), [])
        self.assertEqual(self.repo.find_all_by_user(2), [3])

        self.repo.remove_sticker(1, 1)  # remove something that isnt in the db
        self.assertEqual(self.repo.find_all_by_user(0), [0])
        self.assertEqual(self.repo.find_all_by_user(1), [])
        self.assertEqual(self.repo.find_all_by_user(2), [3])

        self.repo.remove_sticker(2, 3)  # remove something that isnt in the db
        self.assertEqual(self.repo.find_all_by_user(0), [0])
        self.assertEqual(self.repo.find_all_by_user(1), [])
        self.assertEqual(self.repo.find_all_by_user(2), [])


    def test_find_all_by_user(self):
        self.repo.add_sticker(2, 3)
        self.repo.add_sticker(1, 1)
        self.repo.add_sticker(1, 5)
        self.repo.add_sticker(1, 6)
        self.repo.add_sticker(2, 1)
        self.assertEqual(self.repo.find_all_by_user(1), [1, 5, 6])
        self.assertEqual(self.repo.find_all_by_user(2), [1, 3])

    def test_change_username(self):
        before = self.testdb.execute(
            "SELECT name FROM Users WHERE user_id=1").fetchone()
        self.repo.change_username(1, "miki")
        after = self.testdb.execute(
            "SELECT name FROM Users WHERE user_id=1").fetchone()
        self.assertNotEqual(before, after)

    def test_change_action(self):
        before = self.testdb.execute(
            "SELECT action1 FROM Users WHERE user_id=1").fetchone()
        self.repo.change_action(1, 1, 'new action')
        after = self.testdb.execute(
            "SELECT action1 FROM Users WHERE user_id=1").fetchone()
        self.assertNotEqual(before, after)

        before = self.testdb.execute(
            "SELECT action2 FROM Users WHERE user_id=2").fetchone()
        self.repo.change_action(2, 2, 'new action')
        after = self.testdb.execute(
            "SELECT action2 FROM Users WHERE user_id=2").fetchone()
        self.assertNotEqual(before, after)

        before = self.testdb.execute(
            "SELECT action3 FROM Users WHERE user_id=3").fetchone()
        self.repo.change_action(3, 3, 'new action')
        after = self.testdb.execute(
            "SELECT action3 FROM Users WHERE user_id=3").fetchone()
        self.assertNotEqual(before, after)

    def test_find_action(self):
        self.assertEqual(self.repo.find_action(1, 1), 'action1')

    def test_find_username(self):
        self.assertEqual(self.repo.find_username(1), "user1")
        self.assertEqual(self.repo.find_username(2), "user2")
        self.assertEqual(self.repo.find_username(3), "user3")
