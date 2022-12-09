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
        self.db.execute("DELETE FROM UserStickers WHERE user_id=? AND sticker_id=?", [
                        username, sticker])
        self.db.commit()

    def check_ownership(self, username, sticker):
        # checks if a user has a sticker or not
        # returns True if user has sticker, returns False if they don't

        pass

    def change_username(self, user_id:int, username:str):
        """Changes the username of a given user_id.

        Args:
            user_id (int): user_id of the user whose name will be changed
            username (str): a chosen username
        """
        self.db.execute("UPDATE Users SET name=? WHERE user_id=?", [username, user_id])
        self.db.commit()
    
    def change_action(self, user_id:int, action_id:int, action_description:str):
        """Changes the text displayed on the task button.

        Args:
            user_id (int): Current user.
            task_id (int): Which button to change (1, 2 or 3)
            task_description (str): New text.
        """
        if action_id == 1:
            self.db.execute("UPDATE Users SET action1=? WHERE user_id=?", [action_description, user_id])
            self.db.commit()
        elif action_id == 2:
            self.db.execute("UPDATE Users SET action2=? WHERE user_id=?", [action_description, user_id])
            self.db.commit()
        elif action_id == 3:
            self.db.execute("UPDATE Users SET action3=? WHERE user_id=?", [action_description, user_id])
            self.db.commit()
    
    def find_action(self, user_id:int, action_id:int):
        """Find the name of the action from the database. Returns it as a string.

        Args:
            user_id (int): user id as a number
            action_id (int): action id as a number (1,2 or 3)
        """
        if action_id == 1:
            text = self.db.execute("SELECT action1 FROM Users WHERE user_id=?", [user_id]).fetchone()    
        elif action_id == 2:
            text = self.db.execute("SELECT action2 FROM Users WHERE user_id=?", [user_id]).fetchone()    
        elif action_id == 3:
            text = self.db.execute("SELECT action3 FROM Users WHERE user_id=?", [user_id]).fetchone()
        
        return text[0]
            