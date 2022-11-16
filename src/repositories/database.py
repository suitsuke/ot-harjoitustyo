import sqlite3
import os

db = sqlite.connect("stickers.db")
db.isolation_level = None
