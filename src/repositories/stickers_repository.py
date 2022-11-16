import sqlite3
import os

class StickersRepository:
    #controls UserStickers, i.e. who has which stickers
    # (stickers.db should not be modified at any poin by the app)

    def __init__(self, file_path):
        self.db = sqlite3.connect(file_path)
        self.db.isolation_level = None

    def find_by_user(self, username):
        #finds a list of stickers aqcuired by user and returns their id:s in a list
        
        list = []
        
        #todo
        return list
    
    def add_sticker(self, user_id, sticker_id):
        #adds sticker ownership to a user if they don't already have it
        self.db.execute("INSERT INTO UserStickers (user_id, sticker_id) VALUES (?, ?)", [user_id, sticker_id])
        
        #returns what was just put in, in a tuple
        id = self.db.execute("SELECT UserStickers.user_id, UserStickers.sticker_id from UserStickers WHERE UserStickers.user_id=? AND UserSticker.sticker_id=?", [user_id, sticker_id]).fetchone()    
        return id

    def remove_sticker(self, username, sticker):
        #removes sticker ownership from a user (if they own it)
        pass

    def check_ownership(self, username, sticker):
        #checks if a user has a sticker or not
        #returns True if user has sticker, returns False if they don't

        pass
    
