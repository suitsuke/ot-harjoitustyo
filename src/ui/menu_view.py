from tkinter import ttk, constants


class MenuView:
    def __init__(self, root, handle_login, handle_collection, handle_settings):
        self._root = root
        self._handle_login = handle_login
        self._handle_collection = handle_collection
        self._handle_settings = handle_settings
        self._frame = None

        self._initialize()

    def _handle_button_click(self, n):
        button_value = n
        if button_value == 1:
            print("pushed 1")
        elif button_value == 2:
            print("pushed 2")
        elif button_value == 3:
            print("pushed 3")

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="this is the main menu")

        button1 = ttk.Button(
            master=self._frame,
            text="Back to login",
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
            text="Action1",
            command=lambda: self._handle_button_click(1)
        )
        button_a2 = ttk.Button(
            master=self._frame,
            text="Action2",
            command=lambda: self._handle_button_click(2)
        )
        button_a3 = ttk.Button(
            master=self._frame,
            text="Action3",
            command=lambda: self._handle_button_click(3)
        )

        label.grid(row=0, column=0)
        button1.grid(row=3, column=1)  # login
        button2.grid(row=2, column=0)  # collection
        button3.grid(row=2, column=1)  # settings

        button_a1.grid(row=1, column=0)
        button_a2.grid(row=1, column=1)
        button_a3.grid(row=1, column=3)
