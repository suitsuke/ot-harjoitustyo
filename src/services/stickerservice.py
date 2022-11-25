from repositories.stickers_repository import StickersRepository
import sqlite3
import os


class StickerService:
    def __init__(self, user):
        #self.sticker_repo = stickers_repository
        #self.user_repo = user_repository
        default_stickerdb = "data/stickers.db"
        default_userdb = "data/userstickers.db"

        self.user = user
        self.db_stickers = sqlite3.connect(default_stickerdb)
        self.db_userstickers = sqlite3.connect(default_userdb)
        self.repository = StickersRepository(self.db_userstickers)

    def total_stickers(self):
        total_stickers = self.db_stickers.execute(
            "SELECT COUNT(*) FROM Stickers").fetchone()
        total_stickers = total_stickers[0]
        return total_stickers

    def add_sticker(self, user):
        print("pushed 1, user nr:", self.user)
        self.repository
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
