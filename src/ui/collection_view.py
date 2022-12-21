from tkinter import ttk, constants, PhotoImage
from PIL import Image, ImageTk
from services.stickerservice import StickerService
#from tkinter.tix import Balloon


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

    # def display_description(self, id:int):
    #    description = ttk.Label(master=self._frame, text=f"___Sticker-description for {id}")
    #    description.grid(row=6, column=2)

    # def display_empty(self):
    #    description = ttk.Label(master=self._frame, text=f"Hover over a sticker!")
    #    description.grid(row=6, column=2)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        #text and buttons
        label = ttk.Label(master=self._frame, text=f"Your Stickers")

        button = ttk.Button(
            master=self._frame,
            text="To Menu",
            command=self._handle_menu
        )

        label.grid(row=0, column=2, padx=5, pady=(
            15, 0), sticky="e", columnspan=2)
        button.grid(row=5, column=2, padx=5, sticky="e", columnspan=2, pady=20)

        # images
        owned_images = self._service.total_stickers_by_user(self._user)

        # row 1
        if 1 in owned_images:
            image1 = Image.open("data/images/1.png")
        else:
            image1 = Image.open("data/images/0.png")
        photo1 = ImageTk.PhotoImage(image1)
        label1 = ttk.Label(self._frame, image=photo1)
        label1.image = photo1
        label1.grid(row=2, column=1, sticky="e", padx=(30, 0), pady=(20, 0))

        if 2 in owned_images:
            image2 = Image.open("data/images/2.png")
        else:
            image2 = Image.open("data/images/0.png")
        photo2 = ImageTk.PhotoImage(image2)
        label2 = ttk.Label(self._frame, image=photo2)
        label2.image = photo2
        label2.grid(row=2, column=2, pady=(20, 0))

        if 3 in owned_images:
            image3 = Image.open("data/images/3.png")
        else:
            image3 = Image.open("data/images/0.png")

        photo3 = ImageTk.PhotoImage(image3)
        label3 = ttk.Label(self._frame, image=photo3)
        label3.image = photo3
        label3.grid(row=2, column=3, pady=(20, 0))

        if 4 in owned_images:
            image4 = Image.open("data/images/4.png")
        else:
            image4 = Image.open("data/images/0.png")
        photo4 = ImageTk.PhotoImage(image4)
        label4 = ttk.Label(self._frame, image=photo4)
        label4.image = photo4
        label4.grid(row=2, column=4, padx=(0, 30), pady=(20, 0))

        # row2
        if 5 in owned_images:
            image5 = Image.open("data/images/5.png")
        else:
            image5 = Image.open("data/images/0.png")

        photo5 = ImageTk.PhotoImage(image5)
        label5 = ttk.Label(self._frame, image=photo5)
        label5.image = photo5
        label5.grid(row=3, column=1, padx=(30, 0), sticky="e")

        if 6 in owned_images:
            image6 = Image.open("data/images/6.png")
        else:
            image6 = Image.open("data/images/0.png")
        photo6 = ImageTk.PhotoImage(image6)
        label6 = ttk.Label(self._frame, image=photo6)
        label6.image = photo6
        label6.grid(row=3, column=2)

        if 7 in owned_images:
            image7 = Image.open("data/images/7.png")
        else:
            image7 = Image.open("data/images/0.png")
        photo7 = ImageTk.PhotoImage(image7)
        label7 = ttk.Label(self._frame, image=photo7)
        label7.image = photo7
        label7.grid(row=3, column=3)

        if 8 in owned_images:
            image8 = Image.open("data/images/8.png")
        else:
            image8 = Image.open("data/images/0.png")
        photo8 = ImageTk.PhotoImage(image8)
        label8 = ttk.Label(self._frame, image=photo8)
        label8.image = photo8
        label8.grid(row=3, column=4, padx=(0, 30))

        # row3
        if 9 in owned_images:
            image9 = Image.open("data/images/9.png")
        else:
            image9 = Image.open("data/images/0.png")
        photo9 = ImageTk.PhotoImage(image9)
        label9 = ttk.Label(self._frame, image=photo9)
        label9.image = photo9
        label9.grid(row=4, column=1, padx=(30, 0), sticky="e")

        if 10 in owned_images:
            image10 = Image.open("data/images/10.png")
        else:
            image10 = Image.open("data/images/0.png")
        photo10 = ImageTk.PhotoImage(image10)
        label10 = ttk.Label(self._frame, image=photo10)
        label10.image = photo10
        label10.grid(row=4, column=2)

        if 11 in owned_images:
            image11 = Image.open("data/images/11.png")
        else:
            image11 = Image.open("data/images/0.png")
        photo11 = ImageTk.PhotoImage(image11)
        label11 = ttk.Label(self._frame, image=photo11)
        label11.image = photo11
        label11.grid(row=4, column=3)

        if 12 in owned_images:
            image12 = Image.open("data/images/12.png")
        else:
            image12 = Image.open("data/images/0.png")
        photo12 = ImageTk.PhotoImage(image12)
        label12 = ttk.Label(self._frame, image=photo12)
        label12.image = photo12
        label12.grid(row=4, column=4, padx=(0, 30))
