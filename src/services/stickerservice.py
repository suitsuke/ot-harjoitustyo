import sqlite3
import random

from repositories.stickers_repository import StickersRepository


class StickerService:
    def __init__(self):
        default_stickerdb = "data/stickers.db"
        default_userdb = "data/userstickers.db"

        self.db_stickers = sqlite3.connect(default_stickerdb)
        self.db_userstickers = sqlite3.connect(default_userdb)
        self.repository = StickersRepository(self.db_userstickers)

    def total_stickers(self):
        all_stickers = self.db_stickers.execute(
            "SELECT COUNT(*) FROM Stickers").fetchone()
        all_stickers = all_stickers[0]
        return all_stickers

    def add_random_sticker(self, user:int):
        """Pyytää stickers_repositoryä lisäämään random tarran tietylle käyttäjälle.
        Lisää vain sellaisia tarroja, joita käyttäjällä ei ole ennestään.
        Jos kaikki tarrat jo omistetaan, palauttaa -1.

        Args:
            user (_type_): käyttäjä-id, 

        Returns:
            _type_: joko -1 jos tarraa ei lisätty, tai (user_id, sticker_id) jos onnistui
        """
        total = self.total_stickers()
        random_sticker = random.randint(1, total)
        # list of owned stickers sorted by number:
        owned_stickers = self.total_stickers_by_user(user)
        if len(owned_stickers) >= total:
            return -1

        # randomize until you find one that is now owned
        while int(random_sticker) in owned_stickers:
            random_sticker = random_sticker = random.randint(1, total)

        insertion = self.repository.add_sticker(user, random_sticker)
        return insertion

    def add_specific_sticker(self, user, sticker):
        # pyytää stickers_repository lisäämään tietyn tarran tietylle käyttäjälle
        # lisätään vain uusia tarroja joita ei omista
        # jos tarra jo omistetaan: palauttaa -1
        # list of owned stickers by number:
        owned_stickers = self.total_stickers_by_user(user)
        # if len(owned_stickers) >= total:
        #    return -1
        if sticker in owned_stickers:
            return -1

        insertion = self.repository.add_sticker(user, sticker)

        return insertion

    def total_stickers_by_user(self, user):
        # pyytää stickers_repo hakemaan listan tietyn käyttäjän kaikista tarroista
        # lajiteltuna pienestä isompaan
        sticker_list = self.repository.find_all_by_user(user)

        return sticker_list

    def all_stickers(self):
        # hakee listan kaikista tarroista ja niiden tiedoista
        # palauttaa ne jossain muodossa jota ui.collection osaa näyttää
        pass

    def remove_sticker(self, user, sticker):
        # pyytää stickers_repo poistamaan tarran joltain käyttäjältä
        # tämä on ehkä ylimääräinen toiminto, tarpeen jatkokehityksen tarranvaihdossa
        self.repository.remove_sticker(user, sticker)
    
    def change_username(self, user_id:int, username:str):
        """Pyytää repositoryä vaihtamaan käyttäjänimen. Sallittu pituus 1-30 merkkiä.

        Args:
            user_id (int): käyttäjä-id int-muodossa
            username (str): valittu nimi käyttäjälle
        """
        if len(username) >30 or len(username) == 0:
            return -1
        self.repository.change_username(user_id, username)
    
    def change_action(self, user_id:int, action_id:int, action_description:str):
        """Changes the text of the action buttons in the ui.

        Args:
            user_id (int): user_id number
            action_id (int): id-number of the action (1,2 or 3)
            action_description (str): A description of the action. Max length 30.
        """
        if len(action_description) >30:
            return -1
        else:
            self.repository.change_action(user_id, action_id, action_description)

    def find_username(self, user_id:int):
        """Find the the username. Returns as a string.

        Args:
            user_id (int): user-id as number
        """
        return self.repository.find_username(user_id)
    
    def find_action(self, user_id:int, action_id:int):
        """Find the the text for the action buttons. Returns a string.

        Args:
            user_id (int): user-id as number
            action_id (int): action-id as number (1, 2 or 3)
        """
        return self.repository.find_action(user_id, action_id)
