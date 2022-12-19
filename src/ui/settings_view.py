from tkinter import ttk, constants


class SettingsView:
    def __init__(self, root, handle_menu, service, user):
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
        #todo
        entry_value = self._username_entry.get()
        self._service.change_username(self._user, entry_value)
        print("username changed to", entry_value)

    def _handle_userbutton_click(self):
        entry_value = self._username_entry.get()
        self._service.change_username(self._user, entry_value)
        print("username changed to", entry_value)

    def _handle_actionbutton_click(self, number: int):
        if number == 1:
            entry_value = self._action1_entry.get()
        elif number == 2:
            entry_value = self._action2_entry.get()
        elif number == 3:
            entry_value = self._action3_entry.get()

        self._service.change_action(self._user, number, entry_value)
        print("action changed to", entry_value)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="this is the settings")

        back_button = ttk.Button(
            master=self._frame,
            text="Back to Menu",
            command=self._handle_menu
        )
        # Username
        username_label = ttk.Label(master=self._frame, text="Change username")
        self._username_entry = ttk.Entry(master=self._frame)
        username_button = ttk.Button(
            master=self._frame,
            text="Change",
            command=self._handle_userbutton_click
        )
        # Action 1
        action1_label = ttk.Label(master=self._frame, text="Change action 1")
        self._action1_entry = ttk.Entry(master=self._frame)
        action1_button = ttk.Button(
            master=self._frame,
            text="Change",
            command=lambda: self._handle_actionbutton_click(1)
        )
        # Action 2
        action2_label = ttk.Label(master=self._frame, text="Change action 2")
        self._action2_entry = ttk.Entry(master=self._frame)
        action2_button = ttk.Button(
            master=self._frame,
            text="Change",
            command=lambda: self._handle_actionbutton_click(2)
        )
        # Action 3
        action3_label = ttk.Label(master=self._frame, text="Change action 3")
        self._action3_entry = ttk.Entry(master=self._frame)
        action3_button = ttk.Button(
            master=self._frame,
            text="Change",
            command=lambda: self._handle_actionbutton_click(3)
        )

        label.grid(row=0, column=0)
        back_button.grid(row=1, column=0)

        username_label.grid(row=2, column=0)
        self._username_entry.grid(row=2, column=1)
        username_button.grid(row=2, column=2)

        action1_label.grid(row=5, column=0)
        self._action1_entry.grid(row=5, column=1)
        action1_button.grid(row=5, column=2)

        action2_label.grid(row=6, column=0)
        self._action2_entry.grid(row=6, column=1)
        action2_button.grid(row=6, column=2)

        action3_label.grid(row=7, column=0)
        self._action3_entry.grid(row=7, column=1)
        action3_button.grid(row=7, column=2)
