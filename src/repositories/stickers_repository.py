import sqlite3


class StickersRepository:
    # controls UserStickers, i.e. who has which stickers
    # (stickers.db should not be modified at any point by the app)

    def __init__(self, database):
        self.db = database

    def find_all_by_user(self, user):
        # finds a list of stickers aqcuired by user and returns their id:s in a list
        sticker_list = self.db.execute(
            "SELECT sticker_id from UserStickers WHERE user_id=?", [user]).fetchall()
        for i in range(len(sticker_list)):
            sticker_list[i] = int(sticker_list[i][0])

        sorted_list = sorted(sticker_list)
        return sorted_list

    def add_sticker(self, user_id, sticker_id):
        # adds sticker ownership to a user if they don't already have it
        self.db.execute("INSERT INTO UserStickers (user_id, sticker_id) VALUES (?, ?)", [
                        user_id, sticker_id])
        self.db.commit()
        # returns what was just put in, in a tuple
        insertion = self.db.execute("SELECT user_id, sticker_id from UserStickers WHERE user_id=? AND sticker_id=?", [
                                    user_id, sticker_id]).fetchone()
        return insertion

    def remove_sticker(self, username: int, sticker: int):
        # removes sticker ownership from a user (if they own it)
        # return true if successful, false if not
        self.db.execute("DELETE FROM UserStickers WHERE user_id=? AND sticker_id=?", [username, sticker])
        self.db.commit()
        return

    def check_ownership(self, username, sticker):
        # checks if a user has a sticker or not
        # returns True if user has sticker, returns False if they don't

        pass
