from tkinter import ttk, constants, PhotoImage
from PIL import Image, ImageTk

class CollectionView:
    def __init__(self, root, handle_menu, service):
        self._root = root
        self._handle_menu = handle_menu
        self._frame = None
        self._service = service
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        #text and buttons
        label = ttk.Label(master=self._frame, text="this is the collection")

        button = ttk.Button(
            master=self._frame,
            text="Menu",
            command=self._handle_menu
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)


        #images
        #img = PhotoImage(file="data/images/1.gif")
        #image1button = ttk.Button(master=self._frame, image=img, command=lambda:print("image"))
        #image1button.grid(row=2, column=0)
        image = Image.open("data/images/1.gif")
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(self._frame, image=photo)
        label.image = photo
        label.grid(row=3, column=3)
        #ttk.Label(self._frame,image=img).grid(row=3, column=3)

        #pil-images
        #img=ImageTk.PhotoImage(file="data/images/1.gif")
        #img.grid(row=3, column=3)

        
