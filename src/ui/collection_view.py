from tkinter import ttk, constants, PhotoImage
from PIL import Image, ImageTk


class CollectionView:
    def __init__(self, root, handle_menu, service, user):
        self._root = root
        self._handle_menu = handle_menu
        self._frame = None
        self._service = service
        self._user = user
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        #text and buttons
        label = ttk.Label(master=self._frame, text=f"Collection for user {self._user}")

        button = ttk.Button(
            master=self._frame,
            text="Back to menu",
            command=self._handle_menu
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)

        # images
        image1 = Image.open("data/images/1.png")
        photo = ImageTk.PhotoImage(image1)
        label2 = ttk.Label(self._frame, image=photo)
        label2.image = photo
        label2.grid(row=3, column=3)
        
