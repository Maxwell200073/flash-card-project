from tkinter import *


class Btn(Button):
    """Custom tk Button class that allows for darker button images on hover"""
    def __init__(self, root, img1, img2, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.img = img1
        self.img2 = img2

        self['image'] = self.img

        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)

    def enter(self, enter):
        self.config(image=self.img2)

    def leave(self, leave):
        self.config(image=self.img)