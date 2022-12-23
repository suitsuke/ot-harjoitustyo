from tkinter import ttk, constants
from services.stickerservice import StickerService


class MenuView:
    """Päävalikon näkymästä vastaava luokka.
    """

    def __init__(self, root, handle_login, handle_collection, handle_settings, user, service):
        """Päävalikon olion luonti.

        Args:
            root (tkintr-window): Tkinterin pääikkuna
            handle_login (function): kirjautumisnäkymän käynnistävä metodi
            handle_collection (function): kokoelmanäkymän käynnistävä metodi
            handle_settings (function): asetusnäkymän käynnistävä metodi
            user (int): sen hetkisen kirjautuneen käyttäjän id
            service (StickerService): StickerService-olio joka hoitaa ohjelman logiikkaa
        """
        self._root = root
        self._handle_login = handle_login
        self._handle_collection = handle_collection
        self._handle_settings = handle_settings
        self._frame = None
        self.user = user
        self.service = service

        self._initialize()

    def _handle_button_click(self, button_value):
        """Metodi joka huolehtii tarran lisäämisesta kun painetaan tiettyä toimintonappia

        Args:
            button_value (int): Painetun napin numero (1-3)
        """
        if button_value == 1:
            added_sticker = self.service.add_random_sticker(self.user)
        elif button_value == 2:
            added_sticker = self.service.add_random_sticker(self.user)
        elif button_value == 3:
            added_sticker = self.service.add_random_sticker(self.user)
        if added_sticker == -1:
            print("You have collected all stickers!")
        else:
            print("Sticker", added_sticker, "added to user",
                  self.service.find_username(self.user))

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        """Käynnistää graafiset komponentit. Kaikki näytettävät objektit piirretään tässä.
        """
        self._frame = ttk.Frame(master=self._root)
        self._frame.rowconfigure(0, weight=1)
        self._frame.rowconfigure(1, weight=8)
        self._frame.rowconfigure(2, weight=1)

        label = ttk.Label(master=self._frame,
                          text=f"Hello, {self.service.find_username(self.user)}!")

        button1 = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_login
        )

        button2 = ttk.Button(
            master=self._frame,
            text="Collection",
            command=self._handle_collection
        )

        button3 = ttk.Button(
            master=self._frame,
            text="Settings",
            command=self._handle_settings
        )
        button_a1 = ttk.Button(
            master=self._frame,
            text=self.service.find_action(self.user, 1),
            command=lambda: self._handle_button_click(1)
        )
        button_a2 = ttk.Button(
            master=self._frame,
            text=self.service.find_action(self.user, 2),
            command=lambda: self._handle_button_click(2)
        )
        button_a3 = ttk.Button(
            master=self._frame,
            text=self.service.find_action(self.user, 3),
            command=lambda: self._handle_button_click(3)
        )

        label.grid(row=0, column=1, pady=10)
        button1.grid(row=2, column=2, padx=10, pady=10,
                     sticky="nsew")  # login/back
        button2.grid(row=2, column=0, padx=10, pady=10,
                     sticky="nsew")  # collection
        button3.grid(row=2, column=1, padx=10, pady=10,
                     sticky="nsew")  # settings

        button_a1.grid(row=1, column=0, padx=10, pady=5)
        button_a2.grid(row=1, column=1, padx=10, pady=5)
        button_a3.grid(row=1, column=2, padx=10, pady=5)
