from tkinter import Tk
from ui.ui import UI


def main():
    """Käynnistää graafisen käyttöliittymän.
    """
    window = Tk()
    window.title("Stickers")
    window_width = 600
    window_height = 400
    screen_wid = window.winfo_screenwidth()
    screen_hei = window.winfo_screenheight()
    center_x = int(screen_wid/2-window_width/2)
    center_y = int(screen_hei/2-window_height/2)
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
