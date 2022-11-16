import sqlite3
import os

db = sqlite.connect("users_stickers.db")
db.isolation_level = None

#userstickers.db
#contains references on which user_id has which sticker_id
#CREATE TABLE UserStickers (user_id INTEGER REFERENCES Users, sticker_id INTEGER REFERENCES Stickers)


#users.db
#contains information on users, like preferences, name, user-id
#edited by settings
#todo: id, name, button_color

#stickers.db
#contains sticker info
#CREATE TABLE Stickers (id INTEGER PRIMARY KEY, name TEXT, description TEXT);
