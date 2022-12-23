from tkinter import ttk, constants
from services.stickerservice import StickerService


class LoginView:
    """Kirjautumisnäkymän luokka.
    """

    def __init__(self, root, handle_menu, change_user, service):
        """Käynnistää kirjautumisnäkymän olion.

        Args:
            root (tkinter-window): Tkinter-ikkuna
            handle_menu (function): Funktio jolla siirrytään menu-näkymään.
            change_user (function): Funktio, jolla vaihdetaan aktiivista käyttäjää.
            service (StickerService): StickerService-olio
        """
        self._root = root
        self._handle_menu = handle_menu
        self._frame = None
        self._change_user = change_user
        self._service = service

        self._initialize()

    def change_user(self, user):
        """Vaihtaa aktiivisen käyttäjän toiseksi

        Args:
            user (int): Uusi käyttäjä-id.
        """
        self._change_user(user)
        self._handle_menu()
        print(f"User {self._service.find_username(user)} logged in.")

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Choose a user")

        user1_button = ttk.Button(
            master=self._frame,
            text=self._service.find_username(1),
            command=lambda: self.change_user(1)
        )
        user2_button = ttk.Button(
            master=self._frame,
            text=self._service.find_username(2),
            command=lambda: self.change_user(2)
        )
        user3_button = ttk.Button(
            master=self._frame,
            text=self._service.find_username(3),
            command=lambda: self.change_user(3)
        )

        label.grid(row=0, column=1, pady=10)
        user1_button.grid(row=1, column=0, padx=10, pady=(10, 20))
        user2_button.grid(row=1, column=1, padx=10, pady=(10, 20))
        user3_button.grid(row=1, column=2, padx=10, pady=(10, 20))
