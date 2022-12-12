
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

        os.remove("data/userstickers.db")

        self.testdb = sqlite3.connect("data/userstickers.db")
        self.testdb.isolation_level = None
        self.testdb.execute(
            "CREATE TABLE UserStickers (user_id INTEGER REFERENCES Users, sticker_id INTEGER REFERENCES Stickers)")
        self.testdb.execute(
            "INSERT INTO UserStickers (user_id, sticker_id) VALUES (0, 0)")
        self.testdb.execute(
            "CREATE TABLE Users (user_id INTEGER, name TEXT, action1 TEXT, action2 TEXT, action3 TEXT)")
        self.testdb.execute(
            "INSERT INTO Users (user_id, name, action1, action2, action3) VALUES (1, 'user1', 'action1', 'action2', 'action3')")
        self.testdb.execute(
            "INSERT INTO Users (user_id, name, action1, action2, action3) VALUES (2, 'user2', 'action1', 'action2', 'action3')")
        self.testdb.execute(
            "INSERT INTO Users (user_id, name, action1, action2, action3) VALUES (3, 'user3', 'action1', 'action2', 'action3')")
        self.service = StickerService()
        self.stickers_amount = 12

    def tearDown(self):
        os.remove("data/userstickers.db")
        self.testdb = sqlite3.connect("data/userstickers.db")
        self.testdb.isolation_level = None
        self.testdb.execute(
            "CREATE TABLE UserStickers (user_id INTEGER REFERENCES Users, sticker_id INTEGER REFERENCES Stickers)")
        self.testdb.execute(
            "INSERT INTO UserStickers (user_id, sticker_id) VALUES (0, 0)")
        self.testdb.execute(
            "CREATE TABLE Users (user_id INTEGER, name TEXT, action1 TEXT, action2 TEXT, action3 TEXT)")
        self.testdb.execute(
            "INSERT INTO Users (user_id, name, action1, action2, action3) VALUES (1, 'user1', 'action1', 'action2', 'action3')")
        self.testdb.execute(
            "INSERT INTO Users (user_id, name, action1, action2, action3) VALUES (2, 'user2', 'action1', 'action2', 'action3')")
        self.testdb.execute(
            "INSERT INTO Users (user_id, name, action1, action2, action3) VALUES (3, 'user3', 'action1', 'action2', 'action3')")

    def test_total_stickers(self):
        # total amount of stickers in db
        self.assertEqual(self.service.total_stickers(), 12)

    def test_total_stickers_by_user(self):
        self.assertEqual(self.service.total_stickers_by_user(1), [])
        self.assertEqual(self.service.total_stickers_by_user(0), [0])
        self.assertEqual(self.service.total_stickers_by_user(2), [])

    def test_add_random_sticker(self):
        # add a random sticker to user 1, in this case nr 5
        self.service.add_random_sticker(1)
        # oletuksena tietokannassa
        self.assertEqual(len(self.service.total_stickers_by_user(0)), 1)
        # ei lisätty mitään
        self.assertEqual(len(self.service.total_stickers_by_user(2)), 0)
        self.assertEqual(
            len(self.service.total_stickers_by_user(1)), 1)  # testattava

        # self.assertEqual(self.service.add_sticker(1), (1,5)) #for testing

    def test_add_specific_sticker(self):
        self.assertEqual(self.service.add_specific_sticker(1, 1), (1, 1))
        self.assertEqual(self.service.add_specific_sticker(1, 1), -1)

    def test_add_all_stickers(self):
        # add stickers full for a user, check that they are added and finally return -1
        for i in range(1, self.stickers_amount+1):
            self.service.add_random_sticker(3)
            self.assertEqual(len(self.service.total_stickers_by_user(3)), i)
        over_added = self.service.add_random_sticker(3)
        self.assertEqual(len(self.service.total_stickers_by_user(3)), 12)
        self.assertEqual(over_added, -1)
        over_added = self.service.add_random_sticker(3)
        self.assertEqual(over_added, -1)

    def test_remove_sticker(self):
        for i in range(1, self.stickers_amount+1):
            self.service.add_random_sticker(3)
            self.assertEqual(len(self.service.total_stickers_by_user(3)), i)
        self.assertEqual(self.service.total_stickers_by_user(3), [
                         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        self.service.remove_sticker(3, 1)
        self.assertEqual(self.service.total_stickers_by_user(3), [
                         2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        self.service.remove_sticker(3, 10)
        self.assertEqual(self.service.total_stickers_by_user(3), [
                         2, 3, 4, 5, 6, 7, 8, 9, 11, 12])

        self.service.remove_sticker(3, 10)
        self.assertEqual(self.service.total_stickers_by_user(3), [
                         2, 3, 4, 5, 6, 7, 8, 9, 11, 12])

    def test_change_user(self):
        before = self.testdb.execute(
            "SELECT name FROM Users WHERE user_id=1").fetchone()
        self.service.change_username(1, "miki")
        after = self.testdb.execute(
            "SELECT name FROM Users WHERE user_id=1").fetchone()
        self.assertNotEqual(before, after)

    def test_change_action_successfully(self):
        before = self.testdb.execute(
            "SELECT action1 FROM Users WHERE user_id=1").fetchone()
        self.service.change_action(1, 1, 'test')
        after = self.testdb.execute(
            "SELECT action1 FROM Users WHERE user_id=1").fetchone()
        self.assertNotEqual(before, after)

    def test_change_action_too_long(self):
        before = self.testdb.execute(
            "SELECT action1 FROM Users WHERE user_id=1").fetchone()
        self.assertEqual(self.service.change_action(
            1, 1, '123456789012345678901234567890+'), -1)
        after = self.testdb.execute(
            "SELECT action1 FROM Users WHERE user_id=1").fetchone()
        self.assertEqual(before, after)

    def test_find_action(self):
        self.assertEqual(self.service.find_action(1, 1), "action1")
        self.service.change_action(2, 2, "test")
        self.assertEqual(self.service.find_action(2, 2), "test")
        self.service.change_action(3, 3, "1234")
        self.assertEqual(self.service.find_action(3, 3), "1234")

    def test_find_username(self):
        self.assertEqual(self.service.find_username(1), "user1")
