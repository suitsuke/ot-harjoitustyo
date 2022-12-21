from tkinter import Tk
from ui.ui import UI


def main():
    """Käynnistää graafisen käyttöliittymän.
    """
    window = Tk()
    window.title("Stickers")
    window.eval('tk::PlaceWindow . center')
    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
