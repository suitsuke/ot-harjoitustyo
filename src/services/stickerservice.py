from repositories.stickers_repository import StickersRepository
import sqlite3
import os


class StickerService:
    def __init__(self):
        #self.sticker_repo = stickers_repository
        #self.user_repo = user_repository
        default_stickerdb = "data/stickers.db"
        default_userdb = "data/userstickers.db"

        self.db_stickers = sqlite3.connect("data/stickers.db")
        self.db_userstickers = sqlite3.connect(default_userdb)
        self.repository = StickersRepository(self.db_userstickers)

    def total_stickers(self):
        all_stickers = self.db_stickers.execute(
            "SELECT COUNT(*) FROM Stickers").fetchone()
        all_stickers = all_stickers[0]
        return all_stickers

    def add_sticker(self, user):
        print("pushed 1, user nr:", user)
        #self.repository
        # pyytää stickers_repository lisäämään random tarran tietylle käyttäjälle

    def all_user_stickers(self, user):
        # pyytää stickers_repo hakemaan tiedon tietyn käyttäjän kaikista tarroista (lista)
        return
        return sticker_list

    def all_stickers(self):
        # hakee listan kaikista tarroista ja niiden tiedoista
        # palauttaa ne jossain muodossa jota ui.collection osaa näyttää
        pass

    def remove_sticker(self):
        # pyytää stickers_repo poistamaan tarran joltain käyttäjältä
        # tämä on ehkä ylimääräinen toiminto?
        pass
