from tkinter import Tk
from ui.collection_view import CollectionView
from ui.login_view import LoginView
from ui.menu_view import MenuView
from ui.settings_view import SettingsView
from services.stickerservice import StickerService


class UI:
    """Graafinen käyttöliittymä, joka kutsuu muita näkymiä. Tällä luokalla on yksi 
    StickerService-olio, joka annetaan argumenttina jokaiselle näkymälle kun niitä kutsutaan.
    """

    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._user = None
        self._service = StickerService()

    def start(self):
        """Käynnistää kirjautumisnäkymän.
        """
        self._show_login_view()

    def _hide_current_view(self):
        """Sulkee sillä hetkellä olevan näkymän.
        """
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _change_user(self, user):
        """Vaihtaa aktiivisen käyttäjän argumenttina annettuun.

        Args:
            user (int): uuden käyttäjän id numerona
        """
        self._user = user

    def _handle_menu(self):
        """Vaihtaa näkymän menu-näkymäksi.
        """
        self._show_menu_view()

    def _handle_login(self):
        """Vaihtaa näkymän kirjautumisnäkymään.
        """
        self._show_login_view()

    def _handle_collection(self):
        """Vaihtaa näkymän kokoelma-näkymään.
        """
        self._show_collection_view()

    def _handle_settings(self):
        """Vaihtaa näkymän asetukset-näkymään.
        """
        self._show_settings_view()

    def _show_login_view(self):
        """Vaihtaa näkymän. Metodit kutsuvat tätä.
        """
        self._hide_current_view()
        self._current_view = LoginView(
            self._root,
            self._handle_menu,
            self._change_user,
            self._service
        )
        self._current_view.pack()

    def _show_menu_view(self):
        """Vaihtaa näkymän. Metodien kutsuttavissa.
        """
        self._hide_current_view()
        self._current_view = MenuView(
            self._root,
            self._handle_login,
            self._handle_collection,
            self._handle_settings,
            self._user,
            self._service
        )

        self._current_view.pack()

    def _show_collection_view(self):
        """Vaihtaa näkymän, metodien kutsuttavissa.
        """
        self._hide_current_view()
        self._current_view = CollectionView(
            self._root,
            self._handle_menu,
            self._service,
            self._user
        )
        self._current_view.pack()

    def _show_settings_view(self):
        """Vaihtaa näkymän, metodien kutsuttavissa.
        """
        self._hide_current_view()
        self._current_view = SettingsView(
            self._root,
            self._handle_menu,
            self._service,
            self._user
        )
        self._current_view.pack()
