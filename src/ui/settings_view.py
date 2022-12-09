from tkinter import ttk, constants


class SettingsView:
    def __init__(self, root, handle_menu, user):
        self._root = root
        self._handle_menu = handle_menu
        self._frame = None
        self._user = user

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="this is the settings")

        button = ttk.Button(
            master=self._frame,
            text="Back to Menu",
            command=self._handle_menu
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)
