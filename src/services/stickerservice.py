import sqlite3
import random

from repositories.stickers_repository import StickersRepository


class StickerService:
    def __init__(self):
        """Luokka joka hoitaa käyttöliittymän interaktion muiden luokkien kanssa.

        Args:
            db_stickers = tarrojen tietokanta, taulu Stickers
            db_userstickers = käyttäjätietojen tietokanta, taulut Users ja UserStickers
            repository = StickersRepository joka käsittelee tietokantoja
        """
        default_stickerdb = "data/stickers.db"
        default_userdb = "data/userstickers.db"

        self.db_stickers = sqlite3.connect(default_stickerdb)
        self.db_userstickers = sqlite3.connect(default_userdb)
        self.repository = StickersRepository(self.db_userstickers)

    def total_stickers(self):
        """Laskee stickers.db-tietokannan tarrojen määrän.

        Returns:
            int: lukumäärä
        """
        all_stickers = self.db_stickers.execute(
            "SELECT COUNT(*) FROM Stickers").fetchone()
        all_stickers = all_stickers[0]
        return all_stickers

    def add_random_sticker(self, user: int):
        """Pyytää stickers_repositoryä lisäämään random tarran tietylle käyttäjälle.
        Lisää vain sellaisia tarroja, joita käyttäjällä ei ole ennestään.
        Jos kaikki tarrat jo omistetaan, palauttaa -1.

        Args:
            user (int): käyttäjä-id numerona

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

    def add_specific_sticker(self, user: int, sticker: int):
        """Pyytää repositoryä lisäämään tietylle käyttäjälle tietyn tarran.
        Lisää vain tarroja, joita ei omisteta ennestään.

        Args:
            user (int): user-id
            sticker (int): sticker-id

        Returns:
            int or tuple: -1 jos tarra omistettiin aiemmin, tuple lisäyksestä jos onnistui
        """

        owned_stickers = self.total_stickers_by_user(user)

        if sticker in owned_stickers:
            return -1

        insertion = self.repository.add_sticker(user, sticker)

        return insertion

    def total_stickers_by_user(self, user: int):
        """Pyytää repositoryä hakemaan listan tietyn käyttäjän kaikista tarroista.

        Args:
            user (int): user-id numerona

        Returns:
            list: kasvavassa järjestyksessä oleva lista tarrojen id:stä
        """
        sticker_list = self.repository.find_all_by_user(user)

        return sticker_list

    def remove_sticker(self, user: int, sticker: int):
        """Pyytää repositoryä poistamaan tietyn tarran tietyltä käyttäjältä.

        Args:
            user (int): käyttäjä-id jolta poistetaan
            sticker (int): tarra-id joka poistetaan
        """
        self.repository.remove_sticker(user, sticker)

    def remove_all_stickers(self, user: int):
        all_stickers = self.total_stickers()
        for i in range(1, all_stickers+1):
            self.remove_sticker(user, i)

    def change_username(self, user_id: int, username: str):
        """Pyytää repositoryä vaihtamaan käyttäjänimen. Sallittu pituus 1-15 merkkiä.

        Args:
            user_id (int): käyttäjä-id int-muodossa
            username (str): valittu nimi käyttäjälle
        Returns:
            int: 1 if successful, -1 if not
        """
        if len(username) > 15 or len(username) == 0:
            return -1
        self.repository.change_username(user_id, username)
        return 1

    def change_action(self, user_id: int, action_id: int, action_description: str):
        """Changes the text of the action buttons in the ui.

        Args:
            user_id (int): user_id number
            action_id (int): id-number of the action (1,2 or 3)
            action_description (str): A description of the action. Max length 30.
        Returns:
            int: 1 if successful, -1 if not
        """
        if len(action_description) > 30:
            return -1

        self.repository.change_action(user_id, action_id, action_description)
        return 1

    def find_username(self, user_id: int):
        """Find the the username. Returns as a string.

        Args:
            user_id (int): user-id as number
        """
        return self.repository.find_username(user_id)

    def find_action(self, user_id: int, action_id: int):
        """Find the the text for the action buttons. Returns a string.

        Args:
            user_id (int): user-id as number
            action_id (int): action-id as number (1, 2 or 3)
        """
        return self.repository.find_action(user_id, action_id)
