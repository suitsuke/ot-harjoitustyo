from repositories.stickers_repository import StickersRepository
import sqlite3
import os
import random


class StickerService:
    def __init__(self):
        #self.sticker_repo = stickers_repository
        #self.user_repo = user_repository
        default_stickerdb = "data/stickers.db"
        default_userdb = "data/userstickers.db"
        test_userdb = "src/tests/userstickers.db"

        self.db_stickers = sqlite3.connect(default_stickerdb)
        self.db_userstickers = sqlite3.connect(test_userdb)
        self.repository = StickersRepository(self.db_userstickers)

    def total_stickers(self):
        all_stickers = self.db_stickers.execute(
            "SELECT COUNT(*) FROM Stickers").fetchone()
        all_stickers = all_stickers[0]
        return all_stickers

    def add_sticker(self, user):
        # pyytää stickers_repository lisäämään random tarran tietylle käyttäjälle
        # lisätään vain uusia tarroja joita ei omista
        # jos kaikki tarrat omistetaan, palauttaa -1
        total = self.total_stickers()
        random_sticker = random.randint(1,total)
        #list of owned stickers by number:
        owned_stickers = self.total_stickers_by_user(user)
        if len(owned_stickers) >= total:
            return(-1)
        #randomize until you find one that is now owned
        while int(random_sticker) in owned_stickers:
            random_sticker = random_sticker = random.randint(1,total)

        #random_sticker = 5 testing
        insertion = self.repository.add_sticker(user, random_sticker)
        
        return insertion
        

    def total_stickers_by_user(self, user):
        # pyytää stickers_repo hakemaan listan tietyn käyttäjän kaikista tarroista
        #lajiteltuna pienestä isompaan
        sticker_list = self.repository.find_all_by_user(user)
        
        return sticker_list

    def all_stickers(self):
        # hakee listan kaikista tarroista ja niiden tiedoista
        # palauttaa ne jossain muodossa jota ui.collection osaa näyttää
        pass

    def remove_sticker(self):
        # pyytää stickers_repo poistamaan tarran joltain käyttäjältä
        # tämä on ehkä ylimääräinen toiminto?
        pass
