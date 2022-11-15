from tkinter import Tk

from collection_view import CollectionView
from login_view import LoginView
from menu_view import MenuView
from settings_view import SettingsView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None
    
    def _handle_menu(self):
        self._show_menu_view()

    def _handle_login(self):
        self._show_login_view()
    
    def _handle_collection(self):
        self._show_collection_view()
    
    def _handle_settings(self):
        self._show_settings_view()

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(
            self._root,
            self._handle_menu
            )
        self._current_view.pack()
    
    def _show_menu_view(self):
        self._hide_current_view()

        self._current_view = MenuView(
            self._root,
            self._handle_login,
            self._handle_collection,
            self._handle_settings
        )

        self._current_view.pack()
    
    def _show_collection_view(self):
        self._hide_current_view()
        self._current_view = CollectionView(
            self._root,
            self._handle_menu
        )
        self._current_view.pack()
    
    def _show_settings_view(self):
        self._hide_current_view()
        self._current_view = SettingsView(
            self._root,
            self._handle_menu
        )
        self._current_view.pack()

window = Tk()
window.title("TkInter example")

ui = UI(window)
ui.start()

window.mainloop()
