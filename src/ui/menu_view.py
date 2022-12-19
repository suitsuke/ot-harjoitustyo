from tkinter import ttk, constants
from services.stickerservice import StickerService


class MenuView:
    def __init__(self, root, handle_login, handle_collection, handle_settings, user, service):
        self._root = root
        self._handle_login = handle_login
        self._handle_collection = handle_collection
        self._handle_settings = handle_settings
        self._frame = None
        self.user = user
        self.service = service

        self._initialize()

    def _handle_button_click(self, button_value):
        if button_value == 1:
            # add sticker
            added_sticker = self.service.add_random_sticker(self.user)
            print("sticker", added_sticker, "added to user", self.user)
        elif button_value == 2:
            added_sticker = self.service.add_random_sticker(self.user)
            print("sticker", added_sticker, "added to user", self.user)
        elif button_value == 3:
            added_sticker = self.service.add_random_sticker(self.user)
            print("sticker", added_sticker, "added to user", self.user)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.rowconfigure(0, weight=1)
        self._frame.rowconfigure(1, weight=8)
        self._frame.rowconfigure(2, weight=1)

        label = ttk.Label(master=self._frame,
                          text=f"Hello, {self.user}!")

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

        label.grid(row=0, column=1)
        button1.grid(row=2, column=2)  # login/back
        button2.grid(row=2, column=0)  # collection
        button3.grid(row=2, column=1)  # settings

        button_a1.grid(row=1, column=0, ipady=10, padx=5, pady=5, sticky="ns")
        button_a2.grid(row=1, column=1)
        button_a3.grid(row=1, column=2)
