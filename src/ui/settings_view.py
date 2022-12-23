from tkinter import ttk, constants


class SettingsView:
    """Luokka joka hoitaa asetus-näkymän toiminnoista.
    """

    def __init__(self, root, handle_menu, service, user):
        """Käynnistää asetus-näkymän luomalla olion.

        Args:
            root (tkinter-window): Pääikkuna tkinter-ikkunana
            handle_menu (function): funktio jota kutsumalla käyttöliittymä vaihtuu takaisin päävalikkoon
            service (Stickerservice-object): Ohjelman StickerService-palvelu
            user (int): Käyttäjätunnus joka on tällä hetkellä kirjautuneena.
        """
        self._root = root
        self._handle_menu = handle_menu
        self._frame = None
        self._user = user
        self._username_entry = None
        self._action1_entry = None
        self._action2_entry = None
        self._action3_entry = None
        self._service = service

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_removebutton_click(self):
        """Metodi jota kutsutaan kun "Remove all stickers"-nappia painetaan.
        """
        self._service.remove_all_stickers(self._user)
        print("All stickers removed!")

    def _handle_userbutton_click(self):
        """Metodi jota kutsutaan kun painetaan nappia jolla vaihdetaan käyttäjänimi.
        """
        entry_value = self._username_entry.get()
        if len(entry_value) > 15:
            print("Maximum length 15 characters.")
            return
        self._service.change_username(self._user, entry_value)
        print("Username changed to", entry_value)

    def _handle_actionbutton_click(self, number: int):
        """Metodi jota kutsutaan kun vaihdetaan toimintonappien tekstejä.

        Args:
            number (int): Toimintonappi jonka tekstiä muutetaan.
        """
        if number == 1:
            entry_value = self._action1_entry.get()
        elif number == 2:
            entry_value = self._action2_entry.get()
        elif number == 3:
            entry_value = self._action3_entry.get()

        if len(entry_value) > 15:
            print("Maximum length 15 characters.")
            return
        changed = self._service.change_action(self._user, number, entry_value)
        if changed == 1:
            print("Action changed to", entry_value)

    def _initialize(self):
        """Näkymän käynnistävä metodi. Kaikki näytettävät objektit tulevat tänne.
        """
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Settings")
        label2 = ttk.Label(
            master=self._frame, text="Change your actions or username. Max. length 15 characters.")

        back_button = ttk.Button(
            master=self._frame,
            text="Back to Menu",
            command=self._handle_menu
        )
        # Username
        username_label = ttk.Label(master=self._frame, text="Change username")
        self._username_entry = ttk.Entry(master=self._frame, width=15)
        username_button = ttk.Button(
            master=self._frame,
            text="Change",
            command=self._handle_userbutton_click
        )
        # Action 1
        action1_label = ttk.Label(master=self._frame, text="Change action 1")
        self._action1_entry = ttk.Entry(master=self._frame, width=15)
        action1_button = ttk.Button(
            master=self._frame,
            text="Change",
            command=lambda: self._handle_actionbutton_click(1)
        )
        # Action 2
        action2_label = ttk.Label(master=self._frame, text="Change action 2")
        self._action2_entry = ttk.Entry(master=self._frame, width=15)
        action2_button = ttk.Button(
            master=self._frame,
            text="Change",
            command=lambda: self._handle_actionbutton_click(2)
        )
        # Action 3
        action3_label = ttk.Label(master=self._frame, text="Change action 3")
        self._action3_entry = ttk.Entry(master=self._frame, width=15)
        action3_button = ttk.Button(
            master=self._frame,
            text="Change",
            command=lambda: self._handle_actionbutton_click(3)
        )
        # Remove all
        remove_button = ttk.Button(
            master=self._frame,
            text="Remove all Stickers",
            command=lambda: self._handle_removebutton_click()
        )

        label.grid(row=0, column=1, pady=10)
        label2.grid(row=1, column=0, pady=10, columnspan=3, padx=5)
        back_button.grid(row=9, column=1, pady=(0, 10))

        username_label.grid(row=2, column=0, padx=(5, 0))
        self._username_entry.grid(row=2, column=1)
        username_button.grid(row=2, column=2, padx=(0, 5))

        action1_label.grid(row=5, column=0, padx=(5, 0))
        self._action1_entry.grid(row=5, column=1)
        action1_button.grid(row=5, column=2, padx=(0, 5))

        action2_label.grid(row=6, column=0, padx=5)
        self._action2_entry.grid(row=6, column=1)
        action2_button.grid(row=6, column=2, padx=(0, 5))

        action3_label.grid(row=7, column=0, padx=5)
        self._action3_entry.grid(row=7, column=1)
        action3_button.grid(row=7, column=2, padx=(0, 5))

        remove_button.grid(row=8, column=1, pady=5)
